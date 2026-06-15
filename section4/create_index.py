import os

from dotenv import load_dotenv
from langchain_neo4j import Neo4jGraph

load_dotenv()
graph = Neo4jGraph(
    url=os.getenv("NEO4J_URI"),
    username=os.getenv("NEO4J_USERNAME"),
    password=os.getenv("NEO4J_PASSWORD"),
)

indexes = [
    "CREATE INDEX movie_title_index IF NOT EXISTS FOR (m:Movie) ON (m.title)",
    "CREATE INDEX movie_release_index IF NOT EXISTS FOR (m:Movie) ON (m.released)",
]

for idx in indexes:
    graph.query(idx)

print("인덱스 생성 완료")