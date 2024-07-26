'''
문제 링크:https://www.acmicpc.net/problem/1018
카테고리: 브루트포스 알고리즘
문제해설: 체스판 다시 칠하기
'''
#dfs탐색이용-재귀적
'''
<w의 상하좌우는 b, b의 상하좌우는 w이어야함>
<(1,1)부터(n,n)까지 모든 경우에서의 다시 칠하는 수 비교하기>
'''
n,m=map(int,input().split())
board=[]
result=[]

for _ in range(n):
  board.append(list(map(input())))

visited=board.copy()

#시작점(i,j)에서 색칠변수선언
for i in range(n-7):
  for j in range(m-7):
    paint_1=0 #시작이 w일때
    paint_2=0 #시작이 b일때


def dfs(x,y):
  global paint_1
  global paint_2

  if x<=-1 or x>m or y<=-1 or y>n:
    return False
  
  if board[x][y]=='w' and visited[x][y]=='w':
    visited[x][y+1]=='b'

    if visited[x][y+1]=='w':
      paint_1+=1

    visited[x][y-1]=='b'
    if visited[x][y-1]=='w':
      paint_1+=1

    visited[x-1][y]=='b'
    if visited[x-1][y]=='w':
      paint_1+=1
      
    visited[x+1][y]=='b'
    if visited[x+1][y]=='w':
      paint_1+=1

    return True
  
  if board[x][y]=='b' and visited[x][y]=='b':
    visited[x][y+1]=='w'

    if visited[x][y+1]=='b':
      paint_2+=1

    visited[x][y-1]=='w'
    if visited[x][y-1]=='b':
      paint_2+=1

    visited[x-1][y]=='w'
    if visited[x-1][y]=='b':
      paint_2+=1
      
    visited[x+1][y]=='w'
    if visited[x+1][y]=='b':
      paint_2+=1
      
    return True
  
  result.append(min(paint_1,paint_2))

print(min(result))
  
