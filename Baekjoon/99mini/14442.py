'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/14442
카테고리: BFS
문제해설: 
벽 부수고 이동하기 2
'''

import sys
from collections import deque

input = sys.stdin.readline

# n by m metrix
# k: 벽을 부술 수 있는 횟수
n, m, k = map(int, input().split())

graph = [list(map(int, input().strip())) for _ in range(n)]

visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

def bfs():

    # (row, col, break_cnt)
    que = deque([(0, 0, 0)])
    while que:
        r, c, break_cnt = que.popleft()
        
        distance = visited[r][c][break_cnt]

        if r == n - 1 and c == m - 1:
            return distance
        
        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nr = r + dr
            nc = c + dc

            # graph의 범위를 넘은 경우
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue

            # 벽일 경우
            if graph[nr][nc]:
                # 벽을 부순 횟수가 최대인 경우
                if break_cnt == k:
                    continue

                # 방문했으면
                if visited[nr][nc][break_cnt + 1]:
                    continue

                visited[nr][nc][break_cnt + 1] = distance + 1
                que.append((nr, nc, break_cnt + 1))
            
            # 벽이 아닌 경우
            else:
                # 방문했으면
                if visited[nr][nc][break_cnt]:
                    continue
                visited[nr][nc][break_cnt] = distance + 1
                que.append((nr, nc, break_cnt))
    
    return -1

print(bfs())
print(*visited, sep='\n')