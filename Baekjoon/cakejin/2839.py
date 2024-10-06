'''
작성자: cakejin
문제 링크:https://www.acmicpc.net/problem/2839
카테고리: 수학, 다이나믹 프로그래밍, 그리디 알고리즘
문제해설: 설탕 배달

주어진 설탕을 3kg, 5kg 봉지를 최소한으로 사용해 나눠 담기
정확하게 nkg을 만들 수 없으면 -1 출력

n = 5*a + 3*b 인 a, b가 존재하지 않으면 -1
존재하면 n = 5*a + 3*(n-a), (n-a)//5 = 0
점화식 f(n) = max(min(f(n-3)+1,f(n-5)+1),-1)

dp-메모제이션
'''

import sys

input = sys.stdin.readline

n = int(input())

memo = [0] * (n + 1)

if n >= 3:
  memo[3] = 1
if n >= 5:
  memo[5] = 1
if n >= 6:
  memo[6] = 2

for i in range(7, n + 1):

  if memo[i - 3] and memo[i - 5]:
    memo[i] = min(memo[i - 3] + 1, memo[i - 5] + 1)
    
  elif not memo[i - 3] and memo[i - 5]:
    memo[i] = memo[i - 5] + 1
  elif memo[i - 3] and not memo[i - 5]:
    memo[i] = memo[i - 3] + 1

if memo[n]:
  print(memo[n])
else:
  print(-1)
