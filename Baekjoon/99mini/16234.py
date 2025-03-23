'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/16234
카테고리
- 구현
- 그래프 이론
- 그래프 탐색
- 시뮬레이션
- 너비 우선 탐색

문제 해설
1. 이웃한 도시의 국경선이 열리는 지 판단
2. 열린 국경선 그래프를 이용하여 bfs -> 연합 국가의 인구 평균, 연합국가 위치 반환
3. 모든 bfs 탐색 후 새로운 국가 인구 메트릭스 생성
4. 국경선이 열리는 경우가 0일 때까지 반복
'''

import sys
from collections import deque

input = sys.stdin.readline

dn = [
    [0, 1],     # left (col)
    [1, 0],     # bottom (row)
    [0, -1],    # right (col)
    [-1, 0],    # top (row)
]

n, l, r = map(int, input().split())

matrix = [
    list(map(int, input().split())) for _ in range(n)
]

visited = [[False for _ in range(n)] for _ in range(n)]

def bfs(
        graph: list[list[list[tuple[int]]]],
        matrix: list[list[int]],
        row: int, 
        col: int
    ) -> tuple[set[tuple[int, int]], int]:
    '''
    :param graph: 양방향 행렬
    :param matrix: 나라별 인구 행렬
    :param row: 시작 행
    :param col: 시작 열
    '''

    q = deque([(row, col)])

    visited_set = set([(row, col)])

    sum_of_visited = matrix[row][col]

    while q:
        curr_row, curr_col = q.popleft()

        for neighborhood in graph[curr_row][curr_col]:
            nr, nc = neighborhood
            if not is_boundary(nr, nc) or (nr, nc) in visited_set:
                continue

            visited[nr][nc] = True
            visited_set.add((nr, nc))
            q.append((nr, nc))
            sum_of_visited += matrix[nr][nc]
    
    return (visited_set, sum_of_visited // len(visited_set))

def is_boundary(row: int, col: int) -> bool:
    return 0 <= row < n and 0 <= col < n

def is_valid():
    continuous = False

    visited = [[False for _ in range(n)] for _ in range(n)]
    graph: list[list[list[tuple[int, int]]]] = [[[] for _ in range(n)] for _ in range(n)]

    for row in range(n):
        for col in range(n):
            for dr, dc in dn:
                nr = row + dr
                nc = col + dc

                if not is_boundary(nr, nc):
                    continue

                # 국경 경계선 열기 l <= diff <= r
                if l <= abs(matrix[nr][nc] - matrix[row][col]) <= r:
                    continuous = True
                    graph[row][col].append((nr, nc))

    if not continuous:
        return continuous
    
    temp_arr: list[tuple[set[tuple[int, int]], int]] = []
    # 병합하기
    for row in range(n):
        for col in range(n):
            if visited[row][col]:
                continue
            visited_set, mean_of_visited = bfs(graph, matrix, row, col)
            temp_arr.append((visited_set, mean_of_visited))

    for temp in temp_arr:
        visited_set, mean_of_visited = temp

        for v_row, v_col in visited_set:
            matrix[v_row][v_col] = mean_of_visited

    return continuous

ret = 0
while is_valid():
    ret += 1

print(ret)