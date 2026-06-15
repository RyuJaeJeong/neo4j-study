import os

import pandas as pd
from dotenv import load_dotenv
from langchain_neo4j import Neo4jGraph
from langchain_neo4j.graphs.graph_document import GraphDocument, Node, Relationship


load_dotenv()
graph = Neo4jGraph(
    url=os.getenv("NEO4J_URI"),
    username=os.getenv("NEO4J_USERNAME"),
    password=os.getenv("NEO4J_PASSWORD"),
)

df = pd.read_csv("./static/csv/movies_tmdb_small.csv")

node_dict = {}
relationship_arr = []
batch_size = 100
tot_rows = len(df)
for start in range(0, tot_rows, batch_size):
    end = min(start + batch_size, tot_rows)
    batch_df = df.iloc[start:end, :]
    for _, row in batch_df.iterrows():
        movie_id = f"movie-{row['id']}"

        # 영화 노드 생성 (이미 존재하는지 확인하여 중복 방지)
        if movie_id not in node_dict:
            # 영화 노드 속성 설정 (추가 속성 포함)
            movie_properties = {
                "id": movie_id,  # 영화 고유 ID
                "title": row['title'],  # 영화 제목
                "released": row['released'],  # 개봉일
                "rating": float(row['rating']) if pd.notna(row['rating']) else None  #  평점 (결측값 처리)
            }

            # 추가 속성 처리: overview, runtime, tagline (결측값 처리)
            if pd.notna(row.get('overview')):
                movie_properties["overview"] = row['overview']

            if pd.notna(row.get('runtime')):
                # runtime이 숫자인 경우 정수로 변환
                try:
                    movie_properties["runtime"] = int(row['runtime'])
                except (ValueError, TypeError):
                    movie_properties["runtime"] = row['runtime']

            if pd.notna(row.get('tagline')):
                movie_properties["tagline"] = row['tagline']

            # 영화 노드 객체 생성
            movie_node = Node(
                id=movie_id,
                type="Movie",  # 노드 유형 지정
                properties=movie_properties
            )

            # 생성된 영화 노드를 딕셔너리에 저장
            node_dict[movie_id] = movie_node

        # 감독 정보 처리 (결측값이 아닌 경우에만)
        if pd.notna(row.get('director')):
            # 여러 감독이 있을 경우 '|'로 구분되어 있으므로 분리하여 처리
            for director in row['director'].split('|'):
                director = director.strip()  # 앞뒤 공백 제거
                director_id = f"person-{director}"  # 감독 ID 생성

                # 감독 노드가 아직 생성되지 않았다면 새로 생성
                if director_id not in node_dict:
                    director_node = Node(
                        id=director_id,
                        type="Person",  # 인물 유형으로 지정
                        properties={"name": director}  # 감독 이름 속성 설정
                    )
                    # 생성된 감독 노드를 딕셔너리에 저장
                    node_dict[director_id] = director_node

                # 감독과 영화 간의 'DIRECTED' 관계 생성
                relationship_arr.append(
                    Relationship(
                        source=node_dict[director_id],  # 관계의 시작점 (감독)
                        target=node_dict[movie_id],     # 관계의 끝점 (영화)
                        type="DIRECTED",  # 관계 유형
                        properties={}  # 추가 속성 (없음)
                    )
                )

        # 배우 정보 처리 (결측값이 아닌 경우에만)
        if pd.notna(row.get('actors')):
            # 여러 배우가 있을 경우 '|'로 구분되어 있으므로 분리하여 처리
            for actor in row['actors'].split('|'):
                actor = actor.strip()  # 앞뒤 공백 제거
                actor_id = f"person-{actor}"  # 배우 ID 생성

                # 배우 노드가 아직 생성되지 않았다면 새로 생성
                if actor_id not in node_dict:
                    actor_node = Node(
                        id=actor_id,
                        type="Person",  # 인물 유형으로 지정
                        properties={"name": actor}  # 배우 이름 속성 설정
                    )
                    # 생성된 배우 노드를 딕셔너리에 저장
                    node_dict[actor_id] = actor_node

                # 배우와 영화 간의 'ACTED_IN' 관계 생성
                relationship_arr.append(
                    Relationship(
                        source=node_dict[actor_id],  # 관계의 시작점 (배우)
                        target=node_dict[movie_id],  # 관계의 끝점 (영화)
                        type="ACTED_IN",  # 관계 유형
                        properties={}  # 추가 속성 (없음)
                    )
                )

        # 장르 정보 처리 (결측값이 아닌 경우에만)
        if pd.notna(row.get('genres')):
            # 여러 장르가 있을 경우 '|'로 구분되어 있으므로 분리하여 처리
            for genre in row['genres'].split('|'):
                genre = genre.strip()  # 앞뒤 공백 제거
                genre_id = f"genre-{genre}"  # 장르 ID 생성

                # 장르 노드가 아직 생성되지 않았다면 새로 생성
                if genre_id not in node_dict:
                    genre_node = Node(
                        id=genre_id,
                        type="Genre",  # 장르 유형으로 지정
                        properties={"name": genre}  # 장르 이름 속성 설정
                    )
                    # 생성된 장르 노드를 딕셔너리에 저장
                    node_dict[genre_id] = genre_node

                # 영화와 장르 간의 'IN_GENRE' 관계 생성
                relationship_arr.append(
                    Relationship(
                        source=node_dict[movie_id],  # 관계의 시작점 (영화)
                        target=node_dict[genre_id],  # 관계의 끝점 (장르)
                        type="IN_GENRE",  # 관계 유형
                        properties={}  # 추가 속성 (없음)
                    )
                )
    print(f"배치 처리 완료: {start+1}~{end}/{tot_rows} 레코드")
nodes = list(node_dict.values())
graph_doc = GraphDocument(
    nodes=nodes,
    relationships=relationship_arr
)
graph.add_graph_documents([graph_doc])
print("그래프 데이터베이스에 저장 완료")