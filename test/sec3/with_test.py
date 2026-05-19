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
    WHERE p.age >= 20
    WITH p
    WHERE p.name CONTAINS '김'
    RETURN p.name AS 이름, p.age AS 나이       
    """
    result = graph.query(query)
    print(result)


if __name__ == "__main__":
    main()