'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/1759
카테고리: 백트레킹
문제해설: 

de0a4e02ca142a3486eec5b902636194bfd5bfc5
기본 백트레킹 풀이

틀린 케이스: 모음이 한 개 이상 포함되지 않은 경우
4 6
b c d f k j

720686c9f0ee2ebc7e7eddc1be7532c13415d28a
모음 한 개 포함
모음이 포함된 경우 isVowel을 True로 설정

틀린 케이스: 자음이 두 개 이상 포함되지 않은 경우
4 6
a i o e c k

5ddaf4b7135b160c6d27ce132686f0c0b748d80f
정답 풀이

모음의 개수를 백트레킹 마다 저장

스택에 모인 암호의 길이가 목표 길이와 같을 경우
모음의 개수가 >=1 and 목표 길이 - 모음의 개수 >= 2 조건 검사

stack에 알파벳을 푸시 -> 이전 모음의 개수에 0 혹은 1을 더함
백트레킹
팝 -> 푸시 전의 모음 개수로 다시 초기화
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