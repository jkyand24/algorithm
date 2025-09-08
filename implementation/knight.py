# ------------------------------ 내 풀이 (16:33~16:48): 정답 

pos = input()
r, c = pos[1], pos[0]
mapping = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8
}
r = int(r)
c = mapping[c]

# 1번: (cur_r+-1, cur_c+-2)
# 2번: (cur_r+-2, cur_c+-1)

count = 0

for dr in [1, -1]:
    for dc in [2, -2]:
        if (1 <= (r + dr) <= 8) and (1 <= (c + dc) <= 8):
                count += 1

for dr in [2, -2]:
    for dc in [1, -1]:
        if 1 <= (r + dr) <= 8 and 1 <= (c + dc) <= 8:
                count += 1 

print(count)

# ------------------------------ 모범 코드 

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)

# ------------------------------ 배운 점 

# input()의 반환값은 str 타입이다. 

# ord(어떤 문자) = 유니코드 정수 값 