'''
문제 링크:https://www.acmicpc.net/problem/3896
카테고리: 수학, 정수론, 이분탐색, 소수판정, 에라토스테네스의 체
문제해설: 소수 사이 수열
'''
import math

test_case=int(input())
data=list(int(input()) for _ in range(test_case))

def prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
      return False
  return True
  
#data값 양 옆으로 소수 찾고 찾으면 큰수-작은수 값 프린트
for i in data:
  if prime(i):
    print(0)

  else:
    length=0
    data_1=i-1
    data_2=i+1
    #data가 소수가 아니므로 양옆으로 1씩증가 or감소하면서
    while not prime(data_1):
      data_1-=1

    while not prime(data_2):
      data_2+=1
      
    length=data_2-data_1

    print(length)


