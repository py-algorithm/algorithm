'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/6221
카테고리
- 다이나믹 프로그래밍
- 브루트포스 알고리즘
- 정렬
- 가장 긴 증가하는 부분 수열: o(n log n)

문제해설
이 문제는 주어진 수열에서 가장 긴 증가하는 부분 수열(LIS)을 찾는 문제입니다. LIS를 찾기 위해 이진 탐색을 활용하여 효율적으로 구현합니다.

1. 입력으로 주어진 수열을 읽어옵니다. 각 원소는 두 개의 정수로 이루어진 튜플입니다.
2. 수열을 첫 번째 원소와 두 번째 원소를 기준으로 오름차순 정렬합니다.
3. 정렬된 수열을 순회하면서 LIS를 찾습니다. LIS를 저장할 리스트를 초기화하고 첫 번째 원소를 추가합니다.
4. 각 원소에 대해 LIS의 마지막 원소와 비교하여 더 큰 경우 LIS에 추가합니다. 그렇지 않은 경우 이진 탐색을 통해 적절한 위치를 찾아 값을 갱신합니다.
5. 이진 탐색은 LIS 리스트에서 현재 원소가 들어갈 위치를 찾는 데 사용됩니다. 이진 탐색을 통해 O(log n) 시간 복잡도로 위치를 찾을 수 있습니다.
6. 최종적으로 LIS 리스트의 길이를 출력합니다. 이 길이가 가장 긴 증가하는 부분 수열의 길이가 됩니다.

> powered by copilot
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
