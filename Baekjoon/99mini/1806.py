'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/1806
카테고리: 누적합, 투 포인터
문제해설: 
'''

import sys

input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 0
prev_sum = 0
min_length = sys.maxsize

while True:
    # 부분합이 목표보다 크거나 같으면 left++
    if prev_sum >= s:
        min_length=min(min_length, right-left)
        prev_sum -= nums[left]
        left +=1
    # right가 마지막에 도착하면 break
    elif right == n:
        break
    # 부분합이 목표보다 작으면 right++
    else:
        prev_sum += nums[right]
        right += 1

print(0 if min_length == sys.maxsize else min_length)