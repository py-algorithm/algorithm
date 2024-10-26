'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/1759
카테고리: 백트레킹
문제해설: 
'''

import sys

input = sys.stdin.readline

l, c = map(int, input().split())
chars = sorted(list(map(str, input().split())))

stack = []

def back(start):
    if len(stack) == l:
        print(*stack, sep="")
        return
    
    for i in range(start, c):
        stack.append(chars[i])
        back(i + 1)
        stack.pop()

back(0)
