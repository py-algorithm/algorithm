'''
문제 링크:https://www.acmicpc.net/problem/1018
카테고리: 브루트포스 알고리즘
문제해설: 체스판 다시 칠하기

dfs탐색이용-큐자료구조, 최단경로

<입력된 NxM크기의 보드를 잘라서 
8x8크기의 체스판 만들기위해 다시 
색칠해야하는 정사각형 최소 개수 구하기>

1. board 2차원 행렬로 입력받기
2. 브루트포스로 8x8나올 수 있는 모든 경우 확인
3. 함수에 board[i][j]시작으로 하는 8x8에서 색칠해야하는 횟수 구하기
  시작이 w,b일때 각각 나눠서
'''
import sys

input = sys.stdin.readline

#NxM
n, m = map(int, input().split())



#입력받은 보드 상태->2차원 배열
board = []

for _ in range(n):
  board.append(list(map(str,input())))

#각 경우의 값 리스트에 넣어서 최소값만 출력하기
result = sys.maxsize

#시작점(i, j)일때 8X8까지만 범위정해서 다시 칠해야하는 칸 개수 세기
def chess(row,col):
  cnt=0

  is_white=board[row][col]=='W'
  
  for i in range(row, row+8):
    for j in range(col, col+8):
        
      #첫 칸 W
      if is_white:
          #W는 홀수번째 행 + 홀수번째 열 or 짝수번째 행 + 짝수번째 열
          if i % 2 == 1 and j % 2 == 1:
            if board[i][j] == 'B':
              cnt += 1
          if i % 2 ==0 and j % 2 == 0:
            if board[i][j] == 'B':
              cnt += 1
          if i % 2 ==1 and j % 2 == 0:
            if board[i][j] == 'W':
              cnt += 1
          if i % 2 == 0 and j % 2 == 1:
            if board[i][j] == 'W':
              cnt += 1
            

      #첫 칸 B
      else:
          #B는 홀수번째 행 + 홀수번째 열 or 짝수번째 행 + 짝수번째 열
          if i % 2 == 1 and j % 2 == 1:
            if board[i][j] == 'W':
              cnt += 1
          if i % 2 ==0 and j % 2 == 0:
            if board[i][j] == 'W':
              cnt += 1
          if i % 2 ==1 and j % 2 == 0:
            if board[i][j] == 'B':
              cnt += 1
          if i % 2 == 0 and j % 2 == 1:
            if board[i][j] == 'B':
              cnt += 1

  return cnt



for i in range(n-7):
  for j in range(m-7):
    result=min(result, chess(i, j))

    print(i, j, result)
    


