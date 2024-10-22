'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/1391
카테고리: 그리디, 정렬
문제해설: 
1. 종료 시간 기준으로 정렬
2. 시간표를 순회
3. 이전 종료 시간(init: 0) 저장하고, 현재 순회 요소의 시작 시간이 이전 종료 시간보다 크면 이전 종료 시간 업데이트 및 result += 1
'''

import sys

input = sys.stdin.readline

n = int(input())

time_table = list(list(map(int, input().split())) for _ in range(n))

time_table.sort(key=lambda x: (x[1], x[0]))

result = 0
prev_end = 0

for t in time_table:
    start, end = t

    if start >= prev_end:
        prev_end = end
        result += 1

print(result)