'''
문제 링크: https://www.acmicpc.net/problem/111021
카테고리: 수학
문제 해설: A + B를 계산합니다.
'''
n=int(input())

for i in range(1,n+1):
  a,b=map(int,input().split())
  print('Case #'+str(i)+':',a+b)
  i+=1
