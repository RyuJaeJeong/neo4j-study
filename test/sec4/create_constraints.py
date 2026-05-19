import os

from dotenv import load_dotenv
from langchain_neo4j import Neo4jGraph

load_dotenv()
graph = Neo4jGraph(
    url=os.getenv("NEO4J_URI"),
    username=os.getenv("NEO4J_USERNAME"),
    password=os.getenv("NEO4J_PASSWORD"),
)

constraints = [
    "CREATE CONSTRAINT movie_id_unique IF NOT EXISTS FOR (m:Movie) REQUIRE m.id IS UNIQUE",
    "CREATE CONSTRAINT person_name_unique IF NOT EXISTS FOR (p:Person) REQUIRE p.id IS UNIQUE",
    "CREATE CONSTRAINT genre_name_unique IF NOT EXISTS FOR (g:Genre) REQUIRE g.id IS UNIQUE"
]

for cons in constraints:
    graph.query(cons)

print("제약 조건 생성 완료")