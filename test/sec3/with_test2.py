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
    WITH p.city AS 도시, AVG(p.age) AS 평균나이
    WHERE 평균나이 >= 35
    RETURN 도시, 평균나이
    ORDER BY 평균나이 DESC       
    """
    result = graph.query(query)
    print(result)


if __name__ == "__main__":
    main()