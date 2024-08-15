'''
문제 링크:https://www.acmicpc.net/problem/2751
카테고리: 정렬
문제해설: 수 정렬하기2
'''

import sys

input=sys.stdin.readline

n=int(input())

m=[int(input()) for _ in range(n)]

arr=sorted(m)

print(*arr,sep='\n')