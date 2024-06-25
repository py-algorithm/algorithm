'''
문제 링크:https://www.acmicpc.net/problem/10866
카테고리:덱
문제해설:덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리
'''
from collections import deque
import sys

n=int(input())
input=sys.stdin.readline

d=deque([])

for i in range(n):
  commends=input().split()
  commend=commends[0]

  if commend=='push_front':
    d.appendleft(commends[1])

  if commend=='push_back':
    d.append(commends[1])

  if commend=='pop_front':
    if d:
      print(d.popleft())
    else:
      print(-1)

  if commend=='pop_back':
    if d:
      print(d.pop())
    else:
      print(-1)

  if commend=='size':
    print(len(d))

  if commend=='empty':
    if d:
      print(0)
    else:
      print(1)

  if commend=='front':
    if d:
      print(d[0])
    else:
      print(-1)

  if commend=='back':
    if d:
      print(d[-1])
    else:
      print(-1)
