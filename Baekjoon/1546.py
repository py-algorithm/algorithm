'''
문제 링크:https://www.acmicpc.net/problem/1546
카테고리:수학, 사칙연산
문제해설: 조작된 성적 평균 구하기
'''
a=int(input())
b=list(map(int,input().split()))

result=0

for i in b:
  result+=i/max(b)*100

print(result/len(b))