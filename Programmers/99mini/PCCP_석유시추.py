'''
작성자: 99mini
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/250136
카테고리: 그래프, BFS
문제 해설: 
'''

from collections import deque

def solution(land):
    answer = 0
    
    global_id = 0
    
    row_n = len(land)
    col_n = len(land[0])
    
    visited = [[0 for _ in range(col_n)] for _ in range(row_n)]
    
    group_value = dict()
    
    def bfs(row, col):
        q = deque([])
        q.append((row, col))
        
        cnt = 1
        
        group_id = visited[row][col]
        
        while q:
            curr_row, curr_col = q.popleft()
            
            for drow, dcol in [(0,-1), (0,1), (1,0), (-1,0)]:
                nrow = drow + curr_row
                ncol = dcol + curr_col
                
                if nrow < 0 or nrow >= row_n or ncol < 0 or ncol >= col_n:
                    continue
                
                if land[nrow][ncol] == 1 and visited[nrow][ncol] == 0:
                    visited[nrow][ncol] = group_id
                    cnt += 1
                    q.append((nrow, ncol))
        
        group_value[group_id] = cnt
    
    for row in range(row_n):
        for col in range(col_n):

            if visited[row][col] == 0 and land[row][col]:
                global_id += 1
                visited[row][col] = global_id
                bfs(row, col)
    
    for col in range(col_n):
        temp = 0
        visitied_id = dict()
        for row in range(row_n):
            if visited[row][col] and not (visited[row][col] in visitied_id):
                temp += group_value[visited[row][col]]
                visitied_id[visited[row][col]] = True
                
        answer = max(answer, temp)
    return answer

res = solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]])

print(res)