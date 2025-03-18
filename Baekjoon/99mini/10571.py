'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/10571
카테고리
    - 다이나믹 프로그래밍
문제 해설
    - 가장 긴 증가하는 부분 수열
'''

import sys

input = sys.stdin.readline

def binary_search_2d(arr: list[list[float]], w: float, c: float):
    '''
    :param arr: [[w_i, c_i]]
    :param w: w is ASC
    :param c: c is DESC
    '''
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = (start + end) // 2

        curr_w, curr_c = arr[mid]

        if  (curr_w < w      and    curr_c > c  ) or \
            (curr_w < w      and    curr_c == c ) or \
            (curr_w == w     and    curr_c > c  ):
            start = mid + 1
        else:
            end = mid

    return end

t = int(input())

for _ in range(t):
    n = int(input())

    diamond_list = list(
        list(map(float, input().split())) for _ in range(n)
    )

    lis = [diamond_list[0]]
    history = [1]

    for (w, c) in diamond_list[1:]:
        last_w, last_c = lis[-1]

        if  (last_w < w     and     last_c > c  ) or \
            (last_w == w    and     last_c > c  ) or \
            (last_w < w     and     last_c == c ):
            lis.append([w, c])
            history.append(len(lis))
        else:
            idx = binary_search_2d(lis, w, c)
            lis[idx] = [w, c]
            history.append(idx + 1)
    
    print(max(history))