### 🚀 [Section 3: Cypher 고급 문법](./section3)
Cypher 쿼리의 고급 구문 들을 살펴봅니다. 
* 🔹 `가변 길이 탐색` : `-[관계타입*최소길이..최대길이]->` 패턴을 이용한 심층 추적 [[STUDY#2605] Cypher 고급문법(1) - 가변길이 경로 탐색](https://velog.io/@finance/STUDY2605-Cypher-고급문법1-가변길이-경로-탐색)
  * 📝 [variable_length_test1.py](./variable_length_test1.py) - 일반적인 가변 길이 경로 탐색 테스트
  * 📝 [variable_length_test2.py](./variable_length_test2.py) - 고정 길이 경로 탐색 테스트
  * 📝 [variable_length_test3.py](./variable_length_test3.py) - 무제한 길이 경로 탐색
* 🔹 `최단 거리 탐색` : `shortestPath((시작노드)-[관계패턴]-(도착노드))` 함수를 활용한 최적 경로 탐색 [[STUDY#2605] Cypher 고급문법(2) - 최단길이 경로탐색](https://velog.io/@finance/STUDY2605-Cypher-고급문법2-최단길이-경로탐색)
  * 📝 [shortest_path_test.py](./shortest_path_test.py) - 두 노드 간의 최단 경로 탐색
  * 📝 [shortest_path_test2.py](./shortest_path_test2.py) - 두 노드 간의 (특정 관계) 최단 경로 탐색
  * 📝 [shortest_path_test3.py](./shortest_path_test3.py) - 길이의 제한이 있는 최단 경로 탐색
* 🔹 `집계 함수` : `COUNT()`, `SUM()`, `COLLECT()` 등 데이터 집계 함수 [[STUDY#2605] Cypher 고급문법(3) - 집계함수](https://velog.io/@finance/STUDY2605-Cypher-고급문법3-집계함수) 
  * 📝 [aggregating_function_test.py](./aggregating_function_test.py) - `COUNT()` 테스트
  * 📝 [aggregating_function_test2.py](./aggregating_function_test2.py) - `AVG()` 테스트
  * 📝 [aggregating_function_test3.py](./aggregating_function_test3.py) - 특정 노드 별 집계 테스트
  * 📝 [aggregating_function_test4.py](./aggregating_function_test4.py) - 관계가 있는 집계 테스트
  * 📝 [aggregating_function_test5.py](./aggregating_function_test5.py) - 가장 평점이 높은 장소
* 🔹 `WITH 절` : 쿼리 중간 결과를 다음 파이프라인으로 전달하기 (`WITH`) [[STUDY#2605] Cypher 고급문법(4) - WITH와 예제 몇가지](https://velog.io/@finance/STUDY2605-Cypher-고급문법4-WITH와-예제-몇가지)
  * 📝 [with_test.py](./with_test.py) - 다음 절로 전달 되는 항목 제한
  * 📝 [with_test2.py](./with_test2.py) - 집계 결과를 토대로 쿼리 추가 
  * 📝 [with_test3.py](./with_test3.py) - 복잡한 관계 예제