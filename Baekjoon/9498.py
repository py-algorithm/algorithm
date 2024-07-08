'''
문제 링크:https://www.acmicpc.net/problem/9498
카테고리:구현
문제해설:시험 점수를 입력받아 구간에 따른 성적 표시하기
'''
n=int(input())

if 90<=n and n<=100:
  print('A')
if 80<=n and n<=89:
  print('B')
if 70<=n and n<=79:
  print('C')
if 60<=n and n<=69:
  print('D')
if n<60:
  print('F')