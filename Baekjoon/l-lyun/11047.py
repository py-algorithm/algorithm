'''
작성자: l-lyun
문제 링크: https://www.acmicpc.net/problem/11047
카테고리: 그리디

k == coin일 때 누락
현재 조건문 k >= coin에서, 기존 답안은 등호 명시 안해줘서 오답 발생
'''
import sys

n, k = map(int, sys.stdin.readline().split())
coins = []

for i in range(n):
    coin = int(sys.stdin.readline())
    coins.append(coin)

coins.sort(reverse=True)
result = 0
for coin in coins:
    cnt = 0
    if (k >= coin):
        cnt = k // coin
        k -= cnt * coin
    result += cnt
    
print(result)