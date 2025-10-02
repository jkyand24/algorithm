# ------------------------------ 배운 점 

# BFS:
 
# 시작점에서부터 "가까운 순서"로 탐색합니다. 마치 물에 돌을 던졌을 때 물결이 퍼져나가는 모습과 같습니다. 거리가 1인 모든 지점을 보고, 그다음 거리가 2인 모든 지점을 보는 식입니다. 
# -> 목표 지점에 처음 도착하면, 그 경로는 항상 최단 거리

# 같은 단계에서 탐색된 노드들은 동일한 거리를 가진다.

# (1) 탐색(queue에 push, 이때 visited로 전환해야 함 (안그러면: 동일 노드를 향해 다른 경로로 온 두 case가 그 노드를 중복해 push하게 됨)) 
# (2) 방문(queue에서 pop) 

# ------------------------------ 모범 코드 

from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque([(0, 0)])

    while queue:
        cx, cy = queue.popleft()
        print(f"cx cy: {cx} {cy}")

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if not(0<=nx<=n-1) or not(0<=ny<=m-1):
                continue

            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[cx][cy] + 1
    
    return graph[n - 1][m - 1]
    
print(bfs())

# ------------------------------ 내 풀이 (16:27~17:20): 우연히 예시 입력에 대해선 정답이 맞았으나 완전히 틀렸음  

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

count = 0

def bfs(x, y):
        
    queue = deque([(x, y)])
    count += 1
    graph[x][y] = 0

    while queue:
        cx, cy = queue.popleft()
        print(f"current cx cy: {cx} {cy}")
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        exists = False
        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]   
            print(f"candidate nx ny: {nx} {ny}")

            if not(0<=nx<=n-1) or not(0<=ny<=m-1):
                continue

            if graph[nx][ny]==1:
                exists = True
                graph[nx][ny] = 0
                if nx == n-1 and ny == m-1:
                    return True
                queue.append((nx, ny))
        if exists:
            count += 1
            print("count += 1")
    return True

bfs(0, 0)

print(count+1)
