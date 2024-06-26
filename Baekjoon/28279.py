'''
문제 링크:https://www.acmicpc.net/problem/28279
카테고리:덱
문제해설:덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리
'''
import sys
from collections import deque

n=int(input())
input=sys.stdin.readline

d=deque([])

for _ in range(n):
  commends=list(map(int,input().split()))
  commend=commends[0]

  if commend=='1 x':
    d.appendleft(commends[1])
  
  if commend=='2 x':
    d.append(commends[1])

  if commend=='3':
    if d:
      d.popleft()
      print(d)
    else:
      print(-1)

  if commend=='4':
    if len(d)==0:
      print(-1)
    else:
      print(d.pop())
  
  if commend=='5':
    print(len(d))

  if commend=='6':
    if d:
      print(0)
    else:
      print(1)

  if commend=='7':
    if d:
      print(d[0])
    else:
      print(-1)

  if commend=='8':
    if d:
      print(d[-1])
    else:
      print(-1)
