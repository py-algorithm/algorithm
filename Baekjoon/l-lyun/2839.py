'''
작성자: l-lyun
문제 링크: https://www.acmicpc.net/problem/2839
카테고리: 수학, 다이나믹 프로그래밍, 그리디
문제 해설: 3으로 뻬주고, 5의 배수인지 판단

5로 먼저 빼주는 상황은 3의 배수일 때 판별 불가능하여 3으로 빼주기 시작 

n을 5와 3을 최소한으로 사용해 표현하는 문제
'''
import sys

n = int(sys.stdin.readline().strip())
result = 0

while True:
  if (n % 5 == 0):
    result += n // 5
    break
  n -= 3
  result += 1
  if (n == 1 or n == 2):
    result = -1
    break

print(result)
