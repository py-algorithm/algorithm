'''
작성자: cakejin
문제 링크:https://www.acmicpc.net/problem/1920
카테고리: 자료 구조, 정렬, 이분 탐색, 해시를 사용한 집합과 맵
문제해설: 수 찾기

1. a,x 모두 정렬 안되어있음
  
2. 집합으로 중복 값 제거

X[i]에 해당하는 a[i]가 존재하면 1, 없으면 0출력

'''

import sys

input = sys.stdin.readline

N = int(input())

A = set(list(map(int, input().split())))

M = int(input())

X = list(map(int, input().split()))


for i in X:
  if i in A:
    print(1)
  else:
    print(0)
    

