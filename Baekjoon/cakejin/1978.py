'''
문제 링크:https://www.acmicpc.net/problem/1978
카테고리:수학, 정수론, 소수판정
문제해설: 소수 개수 구하기
'''
import math
n=int(input())
a=list(map(int,input().split()))
result=0



for i in a:
  if i<2:
    continue
  flag=True

  for j in range(2,int(math.sqrt(i)+1)):
    if i%j==0:
      flag=False
      break
  
  if flag:
    result+=1

print(result)