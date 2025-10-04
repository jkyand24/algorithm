# ------------- 배운 점 

# 재귀 함수 사용 시 return 빼먹지 말기  

# map은 이터레이터임 -> 그 안의 요소들을 한번씩 순회하고(꺼내고) 나면, map 내부가 비어버림

# set()

# ------------- 다른 풀이

def search2(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if target == arr[mid]:
            return "yes"
        elif target < arr[mid]:
            end = mid-1
        else:
            start = mid+1
    return "no"

# ------------- 다른 풀이 2

for x in ml:
    if x in set(nl):
        print("yes", end=" ")
    else:
        print("no", end=" ")

# ------------- 내 풀이 (23:57~00:22): 정답 

import sys

n = int(input())
nl = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
ml = list(map(int, sys.stdin.readline().rstrip().split()))

nl.sort()

def search(arr, x, start, end):
    if start > end:
        return "no"
   
    mid = (start + end) // 2

    if (x == arr[mid]):
        return "yes"
    elif (x < arr[mid]):
        return search(arr, x, start, mid-1)
    else:
        return search(arr, x, mid+1, end)

for x in ml:
    print(search(nl, x, 0, n-1), end=" ")