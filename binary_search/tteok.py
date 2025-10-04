# ------------------------------- 배운 점

# 이진 탐색을 할 대상을 정확히 정하기: 큰 것으로. 
#    내 풀이는 "떡의 개수"에 대한 이진 탐색, 모범 풀이는 "떡의 길이"에 대한 이진 탐색이다.
#    이때, 문제 조건으로부터 "떡의 길이"의 범위가 더 크므로, 이진 탐색은 "떡의 길이"를 대상으로 해야한다.

# 이진 탐색의 start 또는 end 재할당을 통한 탐색 방향성의 변화를 이해하자

# 본격 코드 작성 전에 로직 먼저 계획해야..

# list[a:-1] => 맨 마지막 요소는 제외됨

# import 코드는 맨 위에 놓기 

# ------------------------------- 모범 코드 

import sys

n, m = map(int, input().split())
nl = list(map(int, sys.stdin.readline().rstrip().split()))
nl.sort()

start = 0
end = max(nl)

answer = 0 

while (start <= end):
    mid = (start + end) // 2

    # 손님 주는 양 구하기 
    tteok_sum = 0
    for tteok in nl:
        if tteok > mid:
            tteok_sum += tteok - mid 
    
    # 좌로갈지 우로갈지 정하기 
    if tteok_sum < m: # 좌로: 손님 줄거 모자람 
        end = mid - 1
    else: # 우로: m을 만족.  
        answer = mid # Q. 최대값이 아닐 수 있지 않는가? A. 여기서 멈추는게 아니고, 아래 `start = mid + 1`에 의해 점점더 큰 h값을 찾게 되고, 이것이 while문이 허락하는 안에서 계속될 것이므로, 자연히 최댓값을 찾게 됨.
        start = mid + 1

print(answer)

# ------------------------------- 내 풀이 (01:56~02:24): 정답 출력했지만 데이터 커지면 시간 초과할듯 (비효율)

"""
5  7

15 12 3 8 10

3 8 10 12 15

0, 4
0, 1
1, 1 -> 여기서 찾으니까 8 < 9임 
2, 1

높이 = h일 때,
손님 떡은 
(h < 길이)인 것에 대해 (길이 - h)를 합친 것 만큼이다.

(h < 길이)인 최소 idx = minidx 를 빠르게 탐색.

start > end => arr[end] < target < arr[start] => 원하는 idx는 "start"
"""

n, m = map(int, input().split())

import sys

nl = list(map(int, sys.stdin.readline().rstrip().split()))

nl.sort()

def bin_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return start

for h in range(nl[-1], 0, -1):
    print(f"current h = {h}")
    minidx = bin_search(nl, h, 0, n-1)
    sonnim = 0
    for i in nl[minidx:]:
        print(f"current 떡길이 = {i}")
        sonnim += (i - h)
    print(f"손님: {sonnim}")
    if sonnim >= m:
        print(f"max h = {h}")
        break
