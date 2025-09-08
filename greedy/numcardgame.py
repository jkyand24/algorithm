# ------------------------------ 내 풀이 (23:24 ~ 23:36): 정답 

"""
# 입력 받기
n_row, m_col = map(int, input().split())

matrix = []
for _ in range(n_row):
    matrix.append(list(map(int, input().split())))

# 정답값 탐색
answer = 0
for row in range(n_row):
    # 현재 row에서의 smallest 찾기 
    smallest = 10000
    for col in range(m_col):
        if matrix[row][col] <= smallest:
            smallest = matrix[row][col]

    # 현재의 smallest가 지금까지 중에 제일 크면 answer에 할당
    answer = smallest

# 정답 출력
print(answer)
"""

# ------------------------------ 모범 코드 

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력 받아 확인하기
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력

# ------------------------------ 배운 점

# 입력을 받는 부분과 로직 부분이 꼭 분리되어야 하는 건 아니다.
