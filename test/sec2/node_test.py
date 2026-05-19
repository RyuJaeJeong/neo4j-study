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
    CREATE 
        (p:Person {name: "홍길동", age: 30, email: "hong@example.com"}),
        (a:Person {name: "김철수", age: 25}),
        (b:Person {name: "이영희", age: 28}),
        (c:City {name: "서울", population: 9700000})
    RETURN 
        p, a, b, c    
    """
    result = graph.query(query)
    print(result)


if __name__ == "__main__":
    main()