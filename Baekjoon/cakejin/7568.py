'''
문제 링크:https://www.acmicpc.net/problem/7568
카테고리: 구현, 브루트포스 알고리즘
문제해설: 덩치
1. [[], 2차원 배열로 x, y 입력받기
    ...]
2. 덩치 등수 매기기
3. 덩치 등수 차례로 출력
'''

import sys

input = sys.stdin.readline

n = int(input())

people = []
result=[]


for i in range(n):
  x,y = map(int,input().split())
  people.append((x,y))
#[[55, 185], [58, 183], [88, 186], [60, 175], [46, 155]]
#people[0][0],people[0][1] 비교 people[1][0],people[1][1]

for i in range(n):
  cnt = 1
  for j in range(n):
      if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
        cnt += 1
  result.append(cnt)

print(*result, sep=' ')

  




