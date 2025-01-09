'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/14003
카테고리
- 이분 탐색
- 가장 긴 증가하는 부분 수열: o(n log n)

문제해설

관련 문제
- [백준 6221]: The Bale Tower
- [백준 1365]: 꼬인 전깃줄
- [백준 2568]: 전깃줄 - 2

랜덤 인풋 생성
import random

# Parameters
n = 1_000_000
min_value = -1_000_000_000
max_value = 1_000_000_000
arr = [random.randint(min_value, max_value) for _ in range(n)]
'''
import sys
input=sys.stdin.readline

def binary_search(arr: list[int, int], target: int):
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = (start + end) // 2
        
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid

    return end

n = int(input())
arr = list((map(int, input().split())))

lis = [arr[0]]
history = [1]

for item in arr[1:]:
    if lis[-1] < item:
        lis.append(item)
        history.append(len(lis))
    else:
        idx = binary_search(lis, item)
        lis[idx] = item
        history.append(idx + 1)

result = []
next_len = len(lis)
for i in range(n - 1, -1, -1):
    if next_len == 0:
        break
    if history[i] == next_len:
        result.append(arr[i])
        next_len -= 1

print(len(result))
print(*result[::-1], sep=' ')

