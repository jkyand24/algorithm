# ------------------------------ 내 풀이 (17:50~17:55): 정답

# ------------------------------ 배운 점 

# split(): 인자 없으면 -> 하나 이상의 연속된 공백(띄어쓰기, 탭, 줄바꿈 등)을 기준으로 문자열 나눔

# ------------------------------ 모범 코드

n = int(input())

array = []
for i in range(n):
    name, grade = input().split()
    grade = int(grade)
    array.append((name, grade))

array = sorted(array, key=lambda tup : tup[1])

for i in array:
    print(i[0], end=" ")