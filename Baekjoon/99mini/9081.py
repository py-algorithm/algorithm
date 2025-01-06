'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/9081
카테고리: 수학, 구현, 문자열, 조합론
문제 해설:
'''

def search_next(text):
    len_text = len(text)

    result = list(text)

    for i in range(len_text - 1, 0, -1):
        if text[i - 1] < text[i]:
            for j in range(len_text - 1, i - 1, -1):
                if text[i - 1] < text[j]:
                    result[i - 1], result[j] = result[j], result[i - 1]
                    return result[:i] + result[i:][::-1]
    return ''.join(result)

t = int(input())

for _ in range(t):
    text = input()

    print(*search_next(text), sep="")