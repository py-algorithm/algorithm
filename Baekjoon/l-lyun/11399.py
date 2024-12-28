'''
작성자: l-lyun
문제 링크: https://www.acmicpc.net/problem/11399
카테고리: 그리디, 정렬
문제 해설: 누적 합
'''
import sys

n = int(sys.stdin.readline().rstrip())
times = list(map(int, sys.stdin.readline().split()))

times.sort()

result = 0
tmp = 0
for time in times:
    tmp += time
    result += tmp
print(result)

