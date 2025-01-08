'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/2568
카테고리
- 가장 긴 증가하는 부분 수열: o(n log n)

문제해설
가장 긴 증가하는 부분 수열을 이분 탐색을 통해서 탐색

잘라야 하는 전깃줄: n - len(lis)

관련 문제
- [백준 6221]: The Bale Tower
- [백준 1365]: 꼬인 전깃줄
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

print(n - len(lis))

flag = 0
for a in arr:
    if flag >= len(lis):
        break
    if a != lis[flag]:
        print(a[0])
    else:
        flag = flag + 1