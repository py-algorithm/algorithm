'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/7511
카테고리: 자료 구조, 그래프 이론, 분리 집합
문제 해설
유니온-파인드 문제
'''

def find(disjoint_set, x):
    '''
    부모 찾기
    '''
    if x != disjoint_set[x]:
        return find(disjoint_set, disjoint_set[x])
    return x

def union(disjoint_set, a, b):
    '''
    분리 집합 병합
    '''

    a, b = find(disjoint_set, a), find(disjoint_set, b) 

    if a < b:
        disjoint_set[b] = a
    elif a > b:
        disjoint_set[a] = b
    
    return disjoint_set

t = int(input())

for test_number in range(t):

    print(f"Scenario {test_number + 1}:")

    n = int(input())
    k = int(input())

    disjoint_set = list(i for i in range(n))

    for _ in range(k):
        a, b = map(int, input().split())

        union(disjoint_set, a, b)
        
    m = int(input())

    for _ in range(m):
        a, b = map(int, input().split())
        print(1 if find(disjoint_set, a) == find(disjoint_set, b) else 0)
    
    if test_number + 1 < n:
        print()