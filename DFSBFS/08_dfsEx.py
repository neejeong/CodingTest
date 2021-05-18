# DFS 메서드 정의
def dfs(graph,v,visited):
  # 현재 노드를 방문 처리
  visited[v] = True
  print(v,end=' ')
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]: # 방문하지 않았다면
      dfs(graph, i, visited) # 그 인덱스를 방문처리

graph = [
  [], # 0번 인덱스 비워둠 
  [2,3,8], # 1번 인덱스부터
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
# False로 초기화 (모든 노드를 방문하지 않았다고 설정)
# 1부터 8까지 인덱스 사용, 0은 사용하지 않음
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)