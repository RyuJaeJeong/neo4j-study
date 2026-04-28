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
    MATCH 
        (a:Person {name: "홍길동"}),
        (b:Person {name: "김철수", age: 25})
    CREATE (a)-[r:KNOWS {since: 2020}]->(b)
    RETURN a, b, r    
    """
    result = graph.query(query)
    print(result)


if __name__ == "__main__":
    main()