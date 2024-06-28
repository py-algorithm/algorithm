'''
문제 링크: https://www.acmicpc.net/problem/2753
카테고리: 수학
문제 해설: 윤년을 판별합니다.
'''

n=int(input())

if (n%4==0 and n%100!=0) or (n%400==0):
  print(1)
else:
  print(0)