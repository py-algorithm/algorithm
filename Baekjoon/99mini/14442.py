'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/14442
카테고리: BFS
문제해설: 
벽 뚫고 이동하기 2
'''

import sys
from collections import deque

input = sys.stdin.readline

# n by m metrix
# k: 벽을 부술 수 있는 횟수
n, m, k = map(int, input().split())

graph = [list(map(int, input().strip())) for _ in range(n)]

# [dict({벽을 부순 횟수: 길이})]
visited: list[dict[int, int]] = [[dict() for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

que = deque([(0, 0)])

while que:
    r, c = que.popleft()

    curr_visited = visited[r][c]

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr = r + dr
        nc = c + dc

        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue
        
        for v in curr_visited:
            distance = curr_visited[v]
            # 벽일 경우
            if graph[nr][nc]:
                # 벽을 뚫은 횟수가 최대값인 경우
                if v == k:
                    continue
                if v+1 in visited[nr][nc]:
                    continue
                visited[nr][nc][v+1] = distance + 1
                que.append((nr, nc))
            
            # 벽이 아닌 경우
            else:
                if v in visited[nr][nc]:
                    continue
                else:
                    visited[nr][nc][v] = distance + 1
                    que.append((nr, nc))

print(*visited, sep='\n')

ret = min(visited[n - 1][m - 1][v] for v in visited[n - 1][m - 1]) if visited[n - 1][m - 1] else -1
print(ret)
