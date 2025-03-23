'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/20040
카테고리: 자료 구조, 분리 집합
문제 해설
- 유니온-파인드 문제
- a와 b가 부모가 같은 경우: find(disjoint_set, a) == find(disjoint_set, b)

개선 사항

```python3
# main()
if find(game, a) == find(game, b):
    return i + 1
        
game = union(game, a, b)
```
find함수 호출과 union 함수 호출에서 동일한 find 함수를 2번씩 중복호출하고 있음.
'''

import sys

input = sys.stdin.readline

def find(disjoint_set, x) -> int:
    '''
    부모 찾기
    '''
    if x != disjoint_set[x]:
        return find(disjoint_set, disjoint_set[x])
    return x

def union(disjoint_set, a, b) -> list[int]:
    '''
    분리 집합 병합
    '''

    a, b = find(disjoint_set, a), find(disjoint_set, b) 

    if a < b:
        disjoint_set[b] = a
    elif a > b:
        disjoint_set[a] = b
    
    return disjoint_set


def main():
    n, m = map(int, input().split())

    game = list(i for i in range(n))

    for i in range(m):
        a, b = map(int, input().split())

        if find(game, a) == find(game, b):
            return i + 1
        
        game = union(game, a, b)

    return 0

print(main())
