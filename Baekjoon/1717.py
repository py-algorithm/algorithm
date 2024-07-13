'''
문제 링크:https://www.acmicpc.net/problem/1717
카테고리:자료 구조, 분리 집합
문제해설: 
0 a b: a, b 합집합 연산
1 a b: a, b가 같은 집합이면 yes 아니면 no 반환
'''

n, m = map(int, input().split())

graph: dict[int, set[int]] = dict()

for _ in range(m):
  commend, a, b = map(int, input().split())

  if commend == 0:
    if not graph.get(a):
      graph[a] = set([a])
    if not graph.get(b):
      graph[b] = set([b])

    graph[a].update(graph.get(b))
    graph[b].update(graph.get(a))
  
  elif commend == 1:
    print(graph)

    is_joint = False
    for item in graph[a]:
      if b == item:
        is_joint = True
        break
    
    if is_joint:
      print('yes')
    else:
      print('no')