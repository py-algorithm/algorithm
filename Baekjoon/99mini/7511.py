'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/7511
카테고리: 자료 구조, 그래프 이론, 분리 집합
문제 해설
'''

def generate_disjoint_set(graph, n):
    '''
    분리 집합 생성
    '''
    return list(i for i in range(n))


def is_same_parent(disjoint_set, a, b):
    '''
    같은 집합의 노드인지 판별
    '''

    return disjoint_set[a] == disjoint_set[b]

t = int(input())

for test_number in range(t):

    print(f"Scenario {test_number + 1}:")

    n = int(input())
    k = int(input())

    graph: dict[int, list[int]] = {}

    for i in range(n):
        graph[i] = []

    for _ in range(k):
        a, b = map(int, input().split())

        graph[a].append(b)
        graph[b].append(a)

    disjoint_set = generate_disjoint_set(graph, n)

    m = int(input())

    for _ in range(m):
        a, b = map(int, input().split())

        print(1 if is_same_parent(disjoint_set, a, b) else 0)
    
    if test_number + 1 < n:
        print()


