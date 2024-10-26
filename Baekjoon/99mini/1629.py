'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/1629
카테고리: 수학, 분할 정복
문제 해설:

A^B mod C = A^(B/2) * A^(B/2)     if B is even
          = A^(B/2) * A^(B/2) * A else
'''

def recursive(a, b, c):
  if b == 1:
    return a % c
  
  temp = recursive(a, b // 2, c)

  if b % 2 == 0:
    return (temp * temp) % c
  else:
    return ((temp * temp) % c) * a % c
  
a, b, c = map(int, input().split())
  
print(recursive(a, b, c))