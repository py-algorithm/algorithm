'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/1717
카테고리:자료 구조, 분리 집합
문제해설: 
0 a b: a, b 합집합 연산
1 a b: a, b가 같은 집합이면 yes 아니면 no 반환
'''

n, m = map(int, input().split())

disjoint_set = list(range(n+1))

def find(node: int) -> int:
  if disjoint_set[node] != node:
    disjoint_set[node] = find(disjoint_set[node])
  return disjoint_set[node]

def union(a: int, b: int) -> None:
  disjoint_set[find(b)] = find(a)

for _ in range(m):
  commend, a, b = map(int, input().split())

  if commend == 0:
    union(a, b)
    
  elif commend == 1:
    is_joint = find(a) == find(b)
    
    if is_joint:
      print('yes')
    else:
      print('no')