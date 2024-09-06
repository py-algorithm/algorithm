'''
문제 링크: https://www.acmicpc.net/problem/1330
카테고리: 구현
문제 해설: 두 정수를 비교합니다.
'''
a,b=map(int, input().split())
if a<b:
  print('<')
elif a>b:
  print('>')
elif a==b:
  print('==')