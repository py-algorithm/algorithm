'''
문제 링크:https://www.acmicpc.net/problem/1436
카테고리: 브루트포스 알고리즘
문제해설: 영화감독 숌

6이 적어도 3번 들어가야함
브루트포스->반복문사용
'''
import sys

input=sys.stdin.readline

n=int(input())
cnt=0
result=666


while True:
  if '666' in str(result):
    cnt+=1
  if cnt==n:
    print(result)
    break
  result+=1




