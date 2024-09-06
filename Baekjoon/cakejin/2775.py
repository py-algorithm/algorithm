'''
문제 링크:https://www.acmicpc.net/problem/2775
카테고리: 수학, 구현, 다이나믹 프로그래밍
문제해설: 부녀회장이 될테야
<조건>
a층b호에 살려면 a-1층의 1호부터 b호까지 
사람들의 수의  합만큼 데려와 살아야함
빈 집없음

입력 K층, n호에 몇명이 살고있는지 출력
0층부터, 1호부터 있고 0층의 i호에는 i명 거주

0층9호->9
1층3호->1+2+3=6
2층3호->1층1호+1층2호+1층3호=1+(1+2)+(1+2+3)
dp 이용-> 이전 i번째 항까지 합이 다음 항
'''
#bottom-up
test_case=int(input())

for _ in range(test_case):
  k=int(input())
  n=int(input())

  resident=[[i for i in range(1,n+1)]]

  for i in range(1,k+1):
    temp=[]
    for j in range(1,n+1):
      temp.append(sum(resident[i-1][:j]))
    resident.append(temp)

  print(resident[-1][-1])
