import os

from dotenv import load_dotenv
from langchain_neo4j import Neo4jGraph

load_dotenv()
graph = Neo4jGraph(
    url=os.getenv("NEO4J_URI"),
    username=os.getenv("NEO4J_USERNAME"),
    password=os.getenv("NEO4J_PASSWORD"),
)

# 모든 노드와 관계 삭제
graph.query("MATCH (n) DETACH DELETE n")

# 제약조건 조회 및 삭제
constraints_list = graph.query("SHOW CONSTRAINTS")
for constraint in constraints_list:
    constraint_name = constraint.get("name")
    print(f"constraint {constraint_name}")
    if constraint_name:
        graph.query(f"DROP CONSTRAINT {constraint_name}")

# 모든 인덱스 삭제
indexes = graph.query("SHOW INDEXES")
for index in indexes:
    index_name = index.get("name")
    index_type = index.get("type")
    print(f"index {index_name} : {index_type}")
    if index_name and index_type != "CONSTRAINT":
        graph.query(f"DROP INDEX {index_name}")