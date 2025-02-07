'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/9951
카테고리
    - 자료 구조
    - 문자열
    - 해시를 사용한 집합과 맵
    - 트리를 사용한 집합과 맵
    - 파싱
    - 정규 표현식
문제 해설
1. 정규식을 이용하여 알파벳과 숫자가 아닌 단어 제거
2. 숫자로만 이루어진 단어 제거
'''

import re

while True:
    line = input().lower()

    if line == '#':
        break

    alpha_dict = dict()

    remove_not_word_pattern = r"[^a-z0-9\s]" # 알파벳 숫자가 아닌 경우 제거
    removed_not_word = re.sub(remove_not_word_pattern, "", line)

    words = removed_not_word.split()

    for word in words:
        if re.match(r"^[0-9]*$", word): # 숫자만으로 이루어진 경우 스킵
            continue

        if not word in alpha_dict:
            alpha_dict[word] = True

    print(*sorted(list(alpha_dict.keys())), sep='\n', end='\n\n')