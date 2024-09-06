'''
문제 링크:https://www.acmicpc.net/problem/30802
카테고리:수학, 구현, 사칙연산
문제해설:웰컴키트 최소주문 개수 구하기
'''
#t의 최소묶음 및 p(남으면 안됨)최대 묶음과 한자루씩 몇개 추가하는지
n=int(input())
num_size=list(map(int,input().split())) #list()말고 []쓰면 오류
t,p=map(int,input().split())

result_t=0 #티셔츠 묶음 수 초기화


for i in num_size:
  if i==0:
    pass
  elif i%t==0:
    result_t+=i//t
  else:
    result_t+=i//t+1
    

print(result_t)
print(n//p, n%p)
  
