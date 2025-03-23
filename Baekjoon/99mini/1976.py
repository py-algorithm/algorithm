'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/1976
카테고리: 자료 구조, 그래프 이론, 그래프 탐색, 분리 집합
문제 해설
- 유니온-파인드 문제
- 인접 행렬 방식
'''

import sys

input = sys.stdin.readline

def find(disjoint_set, x) -> int:
    '''
    부모 찾기
    '''
    if x != disjoint_set[x]:
        return find(disjoint_set, disjoint_set[x])
    return x

def union(disjoint_set, a, b) -> list[int]:
    '''
    분리 집합 병합
    '''

    a, b = find(disjoint_set, a), find(disjoint_set, b) 

    if a < b:
        disjoint_set[b] = a
    elif a > b:
        disjoint_set[a] = b
    
    return disjoint_set

n = int(input())
m = int(input())

cities = list(i for i in range(n))

for i in range(n):
    row = list(map(int, input().split()))

    for j, is_connected in enumerate(row):
        if is_connected:
            cities = union(cities, i, j)

dist = list(map(lambda x: find(cities, int(x) - 1), input().split()))

print ('YES' if len(set(dist)) == 1 else 'NO')
