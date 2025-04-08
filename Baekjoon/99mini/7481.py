'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/7481
카테고리
    - 수학
    - 비둘기집 원리
문제 해설
`mod_flag_dict`을 이용하여 나머지가 같은 경우 미리 break
'''

import sys

input = sys.stdin.readline

res = []

t = int(input())

for _ in range(t):
    a, b, s = map(int, input().split())

    if s == 0:
        res.append('0 0')
        continue

    if a > s and b > s:
        res.append("Impossible")
        continue

    high, low, greaterA = (a, b, True) if a > b else (b, a, False)
    limit = s // high

    flag = False

    mod_flag_dict = dict()

    while limit >= 0:
        remain = s - high * limit
        mod = remain % low

        if mod in mod_flag_dict:
            break

        if mod == 0:
            ret = [str(limit), str(remain // low)]
            res.append(" ".join(ret) if greaterA else " ".join(ret[::-1]))
            flag = True
            break
        
        mod_flag_dict[mod] = True

        limit -= 1

    if not flag:
        res.append("Impossible")

print(*res, sep='\n')

