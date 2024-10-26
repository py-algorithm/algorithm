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
stack["isVowel"] = False
stack["password"] = []

def back(start):
    if len(stack["password"]) == l:
        if stack["isVowel"]:
            print(*stack["password"], sep="")
        return
    
    for i in range(start, c):
        stack["password"].append(chars[i])
        prev = stack["isVowel"]
        stack["isVowel"] = prev or chars[i] in vowel

        back(i + 1)

        stack["password"].pop()
        stack["isVowel"] = prev

back(0)