'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/3190
카테고리: 구현, 자료 구조, 시뮬레이션, 덱, 큐
문제해설: 
'''

n = int(input())

k = int(input())

apple = list(list(map(int, input().split()), False) for _ in range(k))

l = int(input())

commands = list(list(map(str, input().split())) for _ in range(k))

time = 0
length = 1
current = [0, 0]
direction = [0, 1]

for command in commands:
  s, c = command
  s = int(s)

  for _ in range(s):
    time += 1
    current = [current[0] + 1 * direction[0], current[1] + 1 * direction[1]]

    if current[0] < 0 or current[0] > n or current[1] < 0 or current[1] > n:
      break

    for a in apple:
      x, y, mask = a

      if not mask and x == current[0] and y == current[1]:
        length += 1
        a[2] = True



