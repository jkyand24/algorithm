# ------------------------------ 내 풀이: 정답 BUT M이 커지면 시간 초과할 것 

""" 
import random

# 사용자 Input

n = 5 #random.randint(2, 1000)
m = 8 # random.randint(1, 10000)
k = 3 # random.randint(1, m)

lst = [2, 4, 5, 4, 6] #  [random.randint(1, 100) for _ in range(n)]

# 로직 

lst2 = sorted(lst, reverse=True)[:2] # 어차피 상위 두 숫자만 필요 
sum = 0 # 더해진 값 
x = 0 # 총 더한 횟수
z = 0 # 한 숫자를 연속으로 더한 횟수

while x < m:
    # 가장 큰 수를 더함 
    sum += lst2[0]
    x += 1
    z += 1

    # k회 연속으로 더했다면, 두번째로 큰 수를 1번 더함 
    if z == k:
        z = 0 # z값 다시 세기 시작
        sum += lst2[1]
        x += 1

print("sum:", sum) 
"""

# ------------------------------ 모범 코드

# N, M, K를 공백을 기준으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 수를 공백을 기준으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort() # 입력 받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result) # 최종 답안 출력

# ------------------------------ 배운 점

# 문제를 이해하는 데 드는 시간을 아까워하지 말자

# 문제에 대한 이해도가 높아질수록, 풀이는 더 간단해질 수 있다 

# 변수 이름을 정하는 데 시간 허비하지 말자 