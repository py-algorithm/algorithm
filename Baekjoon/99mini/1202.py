'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/1202
카테고리
    -  자료 구조
    -  그리디 알고리즘
    -  정렬    
    -  우선순위 큐
문제 해설
우선 순위 큐를 이용하여 tmp 배열에 항상 가치가 큰 순으로 보석을 정렬
'''

import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())

goods = [tuple(map(int, input().split())) for _ in range(n)] # M, V: M = 무게, V = 가치
bags = [int(input()) for _ in range(k)] # C: 최대 무게

goods.sort()
bags.sort()

ret = 0
tmp = []

for bag in bags:
    while goods and goods[0][0] <= bag:
        heapq.heappush(tmp, -goods[0][1])
        heapq.heappop(goods)
    if tmp:
        ret -= heapq.heappop(tmp)
print(ret)