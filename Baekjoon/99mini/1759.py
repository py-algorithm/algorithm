'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/1759
카테고리: 백트레킹
문제해설: 
'''

import sys

input = sys.stdin.readline

vowel = ["a", "e", "i", "o", "u"]

l, c = map(int, input().split())
chars = sorted(list(map(str, input().split())))

stack = dict()
stack["vowel_cnt"] = 0
stack["password"] = []

def back(start):
    if len(stack["password"]) == l:
        if stack["vowel_cnt"] >= 1 and l - stack["vowel_cnt"] >= 2:
            print(*stack["password"], sep="")
        return
    
    for i in range(start, c):
        stack["password"].append(chars[i])
        prev = stack["vowel_cnt"]
        stack["vowel_cnt"] = prev + (1 if chars[i] in vowel else 0)

        back(i + 1)

        stack["password"].pop()
        stack["vowel_cnt"] = prev

back(0)