# ------------------------------ 내 코드 (시간 아득히 초과): 정답

r, c = map(int, input().split()) # 크기

y, x, d = map(int, input().split()) # 현재 좌표

m = []

for _ in range(r):
    _r = list(map(int, input().split()))
    m.append(_r) # m의 i번째 요소는 row=i에서의 가로 한 줄 

visited = [(y, x)]

def is_valid(tup):
    if not ((0<=tup[0]<=r-1) and (0<=tup[1]<=c-1)): # 아예 맵 밖이면 
        return False
    return (tup not in visited) and (m[tup[0]][tup[1]] == 0)

def pos_of_d(y, x, d):
    d = d % 4

    if d == 0:
        return (y-1, x)
    if d == 1:
        return (y, x+1)
    if d == 2:
        return (y+1, x)
    if d == 3:
        return (y, x-1)
    
def left_d(d):
    return (d-1) % 4

while True:
    # 왼쪽 방향에 '가보지 않은' & '육지인' 칸이 있다면
    if is_valid(pos_of_d(y, x, left_d(d))):
        d = left_d(d)
        y, x = pos_of_d(y, x, d)
        visited.append((y, x))
    # 없다면
    else: 
        # 아직 돌아볼 방향이 남았다면
        if is_valid(pos_of_d(y, x, left_d(d-1))) or is_valid(pos_of_d(y, x, left_d(d-2))) or is_valid(pos_of_d(y, x, left_d(d-3))):
            d = left_d(d)
            continue
        # 이젠 어디로도 갈 수 없다면
        else: 
            # 뒤가 육지라면
            (y_, x_) = pos_of_d(y, x, left_d(d-1))
            if (0<=y_<=r-1) and (0<=x_<=c-1):
                if m[y_][x_] == 0:
                    y, x = y_, x_
                    visited = visited.append((y, x)) if ((y, x) not in visited) else visited
                else:
                    break
            # 뒤가 바다라면
            else:
                break
            
print(len(visited))
print(visited)

# ------------------------------ 모범 코드

# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)

# ------------------------------ 개선한 내 코드

n, m = map(int, input().split())

a, b, d = map(int, input().split())

array = []
for _ in range(n):
    line = list(map(int, input().split()))
    array.append(line)

def left_d(d):
    return (d-1) % 4

dx = [0, +1, 0, -1]
dy = [-1, 0, +1, 0]

def is_0(a, b):
    if not (0 <= a <= n-1):
        return False
    if not (0 <= b <= m-1):
        return False
    return (array[a][b] == 0)

visited = [[0] * m for _ in range(n)]
visited[a][b] = 1
print(visited)

turn_count = 0

while True:
    d = left_d(d)
    turn_count += 1

    na, nb = a + dy[d], b + dx[d]
    print("na, nb:", na, nb)

    # 왼쪽 방향에 valid:
    if (visited[na][nb] == 0) and is_0(na, nb):
        a, b = na, nb
        visited[a][b] = 1
        print("방문:", a, b)
        turn_count = 0
       
    if turn_count == 4:
        na, nb = a - dy[d], b - dx[d]

        if is_0(na, nb):
            a, b = na, nb
            visited[a][b] = 1
            print("방문:", a, b)
            turn_count = 0
            continue
        
        else:
            break

print("visited:", visited)
count = sum(val == 1 for row in visited for val in row)
print(count) 

# ------------------------------ 배운 점 

# 방향을 설정해 이동하는 문제에서는 dx, dy 리스트를 만들어놓고 사용하는 게 편리. 

# 방문 횟수가 아니라 방문 여부 (즉, 숫자가 아니라 True/False) 정보를 가져야 하는 경우, 
# 굳이 방문 좌표 리스트보단, 맵 상에 0/1로 표시

# 문제를 곧이곧대로 코드로 옮기기보다는, 깊이 이해해봤을 때 원리상 간단히할 수 있는 부분을 찾기 

# 리스트 인덱싱 조심

# % 사용 시 나누는 값 조심 