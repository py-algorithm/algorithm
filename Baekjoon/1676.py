'''
문제 링크:https://www.acmicpc.net/problem/1676
카테고리: 수학
문제해설: 팩토리얼 0의 개수

n!에서 뒤에서 부터 처음 0이 아닌 수가 나올 때 까지 
0의 개수 구하기

'''
import sys

input = sys.stdin.readline

n = int(input())
factorial_n = 1
cnt = 0

for i in range(1,n+1):
  if n == 0:
    break
  factorial_n *= i
  i += 1

arr = []

while(factorial_n != 0):
  arr.append(factorial_n%10)
  factorial_n = factorial_n//10

for i in range(len(arr)):
  if arr[i] == 0:
    cnt += 1
  
print(cnt)
    

