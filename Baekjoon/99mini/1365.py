'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/1365
카테고리
- 이분 탐색
- 가장 긴 증가하는 부분 수열: o(n log n)

문제해설
가장 긴 증가하는 부분 수열을 이분 탐색을 통해서 탐색
n - len(lis) 값을 출력

관련 문제
- [백준 6221]: The Bale Tower
'''

def binary_search(arr: list[int, int], target: int):
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = (start + end) // 2
        
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid

    return end

n = int(input())
arr = list((map(int, input().split())))

lis = [arr[0]]

for item in arr[1:]:
    if lis[-1] < item:
        lis.append(item) 
    else:
        idx = binary_search(lis, item)
        lis[idx] = item

print(n - len(lis))