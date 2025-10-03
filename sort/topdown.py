# ------------------------------ 배운 점 

# sorted()의 reverse 파라미터

# print()의 end 파라미터

# 정수 하나만 받을때는 map(int, input()) 말고 int(input())

# list 요소 자체를 iter할 거면, 
# 그냥 for i in array: print(i)

# 가능하다면 굳이 새 변수 정의 X. 

# ------------------------------ 내 풀이 (17:35~17:41): 정답이지만, print()의 end 파라미터 활용 못했었음 

# ------------------------------ 모범 코드
n = int(input())

nums = []
for _ in range(n):
    nums.append(int(input()))

nums = sorted(nums, reverse=True)

for i in nums:
    print(i, end=" ")