'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/12852
카테고리: DP
문제 해설

1. dp에 연산자의 결과값을 저장
2. dp를 n부터 0까지 순회하며 dp에 기록된 값이 내림차순이 될 수 있는 인덱스를 Path에 저장

'''

n = int(input())

dp = [0] * (10**6 + 1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    
path = [n]
curr = n
temp = dp[n] - 1

for i in range(n, 0, -1):
    if dp[i] == temp and (i + 1 == curr or i * 2 == curr or i * 3 == curr):
        curr = i
        path.append(i)
        temp -= 1

print(dp[n])
print(*path)
