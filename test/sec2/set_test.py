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
    MATCH (p:Person {name: "홍길동"})
    SET p.age = 35        
    RETURN p    
    """
    result = graph.query(query)
    print(result)


if __name__ == "__main__":
    main()