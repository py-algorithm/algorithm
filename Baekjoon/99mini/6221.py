'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/6221
카테고리
- 다이나믹 프로그래밍
- 브루트포스 알고리즘
- 정렬
- 가장 긴 증가하는 부분 수열: o(n log n)

문제해설
Input
```
6
6 9
10 12
9 11
8 10
7 8
5 3
```
Hint
```
10 12
9 11
8 10
6 9
5 3
```
-> 5
'''

def binary_search(arr: list[tuple[int, int]], target: tuple[int ,int]):
    a, b = target

    start = 0
    end = len(arr) - 1

    while start < end:
        mid = (start + end) // 2

        arr_a, arr_b = arr[mid]
        
        if arr_a < a and arr_b < b:
            start = mid + 1
        else:
            end = mid

    return end

n = int(input())

arr = []

for i in range(n):
    arr.append(tuple(map(int, input().split())))

arr.sort(key = lambda x: (x[0], x[1]))

lis = [arr[0]]

for item in arr:
    a, b = item
    if lis[-1][0] < a and lis[-1][1] < b:
        lis.append((a, b)) 
    else:
        idx = binary_search(lis, (a, b))
        lis[idx] = (a, b)


print(len(lis))
