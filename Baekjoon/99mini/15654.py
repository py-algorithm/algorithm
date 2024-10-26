'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/15654
카테고리: 백트래킹
문제해설: 
'''

n, m = map(int, input().split())

l = sorted(list(map(int, input().split())))

def back(origin: list[int], output: list[int]):
  if len(output) == m:
    print(*output, sep=' ')
  
  for i in origin:
    if i not in output:
      output.append(i)
      back(origin, output)
      output.pop()

back(l, [])

