# ---------- 배운 점 

# 변수 이름은 최대한 짧게 

# ~~을 "몇번 해야 한다" != "최대 몇번 할 수 있다"

# sum(리스트): 리스트의 모든 원소의 합 출력 

# ---------- 모범 답안 

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if (a[i] < b[i]):
        a[i], b[i] = b[i], a[i]
    else: 
        break

print(sum(a))

# ---------- 내 답안: 문제를 약간 오해했음.. 