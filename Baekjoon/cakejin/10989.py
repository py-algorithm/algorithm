'''
문제 링크:https://www.acmicpc.net/problem/10989
카테고리: 정렬
문제해설: 수 정렬하기3

시간, 메모리 초과 주의!->sys사용

계수 정렬 이용 : 동일한 값을 가진 데이터가 여러 개 일 떄 효과적
'''
import sys
input=sys.stdin.readline

n=int(input())
max_num = 10_001
arr=[0]*max_num 

for _ in range(n):
  i=int(input())
  arr[i]+=1

for i in range(max_num):
  if arr[i] > 0:
     for _ in range(arr[i]):
        print(i)
