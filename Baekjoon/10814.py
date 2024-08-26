'''
문제 링크:https://www.acmicpc.net/problem/10814
카테고리: 정렬
문제해설: 나이순 정렬
가입한 회원의 나이 순으로 정렬
나이가 같으면 먼저 가입한 순으로 정렬

2차원 배열 정렬 -> lamda이용
'''
import sys

input=sys.stdin.readline

n=int(input())
club = []

for i in range(n):
  x,y = list(map(str, input().split()))
  x = int(x)
  club.append((x,y))
#[(21, 'Junkyu'), (21, 'Dohyun'), (20, 'Sunyoung')]
#club[0][i]<>=club[0][j]

club.sort(key=lambda x:x[0])#2차원 배열 정렬

for i in club:
  print(i[0], i[1])



