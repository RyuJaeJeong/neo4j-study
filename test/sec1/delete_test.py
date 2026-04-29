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
    MATCH (p:Person {name: "이영희"})
    // DELETE p  
    DETACH DELETE p  
    """
    result = graph.query(query)
    print(result)


if __name__ == "__main__":
    main()