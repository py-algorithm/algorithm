'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/3896
카테고리: 수학, 정수론, 이분 탐색, 소수 판정, 에라토스테네스의 체
문제 해설
예시
k = 27
27보다 작은 소수 23
27보다 큰 소수 29

=> { 24, 25, 26, 27, 28 } n - 1 = 5

입력 예시
5
10
11
27
2
492170

출력 예시
4
0
6
0
114
'''
max_range=1299709

primary = [False,False] + [True] * (max_range - 1)

for i in range(2, max_range+1):
  if primary[i]:
    for j in range(2*i, max_range+1, i):
        primary[j] = False

t = int(input())

for _ in range(t):
  k = int(input())

  if primary[k]:
    print(0)
    continue

  result = 0
  for i in reversed(range(2, k)):
    if primary[i]:
      break
    result += 1

  for i in range(k, max_range):
    if primary[i]:
      break
    result += 1

  print(result + 1)