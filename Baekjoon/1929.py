'''
문제 링크:https://www.acmicpc.net/problem/1929
카테고리:수학
문제해설:소수구하기-에라토스테네스의체
'''

import math

m,n=map(int,input().split())

arr=[True for i in range(n+1)] #m부터가아님
arr[1]=False#이 조건 없으면 1 1입력시 1출력됨-미미

for i in range(2,int(math.sqrt(n)+1)):#m부터가아니라 2부터
  if arr[i]:
    j=2
    while i*j<=n:
      arr[i*j]=False
      j+=1

for i in range(m,n+1):
  if arr[i]:
    print(i)