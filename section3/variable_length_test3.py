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
    MATCH (p1:Person {name: '홍길동'})-[r:KNOWS*]->(p2:Person)
    RETURN p1.name AS 시작점, p2.name AS 도착점, size(r) AS 관계의_수        
    """
    result = graph.query(query)
    print(result)


if __name__ == "__main__":
    main()