'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/2805
카테고리: 이분 탐색
문제해설
left(=1)와 right(=max(trees)를 두어 이분 탐색
'''

import sys

input = sys.stdin.readline

def binary(trees, len_tree, m, left, right):
    mid = (left + right) // 2
    if(left > right):
        return mid
    sum_of_tree = 0
    for i in range(len_tree):
        if(trees[i] - mid > 0):
            sum_of_tree += trees[i] - mid
    if(sum_of_tree < m):
        return binary(trees, len_tree, m, left, mid - 1)
    elif(sum_of_tree > m):
        return binary(trees, len_tree, m, mid + 1, right)
    else:
        return mid


n, m = map(int, input().split())
trees = list(map(int, input().split()))

ret = binary(trees, len(trees), m, 1, max(trees))

print(ret)