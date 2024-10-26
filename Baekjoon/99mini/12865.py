'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/12865
카테고리: 배낭 문제, DP
문제해설:

점화식

bag: dict[str, int]
dp[i][w] = max(dp[i-1][w], bag.v + dp[i-1][w-bag.w]) if (w >= bag.w)
         = dp[i-1][w]                                else

실패 코드
```
n, k = map(int, input().split())

dp = [[0 for _ in range(k+1)] for _ in range(n)]

for i in range(n):
  w, v = map(int, input().split())

  for j in range(1, k+1):
    if j >= w:
      dp[i][j] = max(dp[i-1][j], v + dp[i-1][j-w]) # dp[i-1] 접근 시 i = 0 인 경우 dp[-1]을 접근하며 실패
    else:
      dp[i][j] = dp[i-1][j]

print(dp[n-1][k])
```
'''

n, k = map(int, input().split())

dp = [[0 for _ in range(k + 1)] for _ in range(n+1)]

for i in range(1, n + 1):
  w, v = map(int, input().split())

  for j in range(1, k + 1):
    if j >= w:
      dp[i][j] = max(dp[i - 1][j], v + dp[i - 1][j - w])
    else:
      dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])