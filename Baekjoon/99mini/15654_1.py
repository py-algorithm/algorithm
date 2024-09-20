'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/15654
카테고리: 백트래킹
문제해설: 결과값 저장하는 버전
'''

n, m = map(int, input().split())

l = sorted(list(map(int, input().split())))

def back(origin: list[int], output: list[int]) -> list[list[int]]:
  result = []
  
  if len(output) == m:
    result.append(output[:])
    return result

  for i in origin:
    if i not in output:
      output.append(i)
      result += back(origin, output)
      output.pop()

  return result

ret = back(l, [])
for r in ret:
  print(*r, sep=' ')

