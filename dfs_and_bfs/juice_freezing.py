# ------------------------------ 내 풀이: 노답

# ------------------------------ 모범 코드

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result) # 정답 출력

# ------------------------------ 배운 점

# DFS, BFS 모두 가능하다. (인접한 부분으로 퍼져나가는 동작이기에)

# 위 로직에서는 중복 count를 걱정할 필요가 없음: 
# 결국엔 각 노드에 대해 dfs 결과가 True이냐 아니냐를 count할 뿐인데,
# 임의 노드가 already visited인 경우, dfs는 무조건 False임.
# (이 노드가 already visited로 전환된 이유: 이전의 dfs에 의해 해당 노드가 graph[x][y] = 1
# 즉, 이전의 dfs 동작을 통해 도달할 수 있는 위치였다면, 즉 같은 얼음 덩어리라면, visited됨)

# DFS, BFS를 꼭 ->, ↓ 방향으로만 수행할 필요는 없다.  

# 주어진 문제를 해결하기 위해서 visited 정보를 활용할수도 있다.