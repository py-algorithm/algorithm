'''
문제 링크:https://www.acmicpc.net/problem/2475
카테고리:수학, 구현, 사칙연산
문제해설:주어진 조건대로 연산된 검증수 출력하기
'''
'''a=map(int,input().split())
result=0

for i in a:
  result+=i**2

print(result%10)
'''

from functools import reduce

ret=reduce(lambda acc, cur : acc + cur**2, map(int,input().split()),0)%10

print(ret)