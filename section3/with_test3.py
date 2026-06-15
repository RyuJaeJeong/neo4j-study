import os
from dotenv import load_dotenv

from langchain_neo4j import Neo4jGraph

load_dotenv()
graph = Neo4jGraph(
    url=os.getenv("NEO4J_URI"),
    username=os.getenv("NEO4J_USERNAME"),
    password=os.getenv("NEO4J_PASSWORD"),
)


def main():
    query = """\
    MATCH (p:Person)
	OPTIONAL MATCH (p)-[:VISITED]->(l:Location)
	WITH p, COUNT(DISTINCT l) AS 방문장소수
	OPTIONAL MATCH (p)-[:LIKES]->(i:Interest)
	WITH p, 방문장소수, COUNT(DISTINCT i) AS 관심분야수
	WHERE 방문장소수 >= 2 AND 관심분야수 >= 2
	RETURN p.name AS 이름, 방문장소수, 관심분야수       
    """
    result = graph.query(query)
    print(result)


if __name__ == "__main__":
    main()