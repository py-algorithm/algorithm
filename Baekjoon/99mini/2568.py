'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/2568
카테고리
- 가장 긴 증가하는 부분 수열: o(n log n)

문제해설
가장 긴 증가하는 부분 수열을 이분 탐색을 통해서 탐색

잘라야 하는 전깃줄: n - len(lis)

history 리스트는 해당 인덱스의 가장 긴 증가하는 부분 수열의 길이(length)를 기록한다.

lis가 완성되면 뒤에서부터 순회하여 가장 긴 증가하는 부분 수열에 해당하지 하는 경우 arr[i]의 첫 번째 값(a 타워)의 값을 -1로 스위치한다.

arr[i][0]가 -1이 아닌 경우 자른 전깃줄임으로 arr[i][0]을 출력한다.

관련 문제
- [백준 6221]: The Bale Tower
- [백준 1365]: 꼬인 전깃줄

레퍼런스
- https://kukekyakya.tistory.com/222 잘라야하는 전깃줄 출력하기
- https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4 개념 학습
'''

def binary_search(arr: list[list[int, int]], target: list[int ,int]):
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
    arr.append(list(map(int, input().split())))

arr.sort(key = lambda x: (x[0]))

lis = [arr[0]]
history = [1]

for item in arr[1:]:
    a, b = item
    if lis[-1][0] < a and lis[-1][1] < b:
        lis.append((a, b))
        history.append(len(lis))
    else:
        idx = binary_search(lis, (a, b))
        lis[idx] = (a, b)
        history.append(idx + 1)

print(n - len(lis))

len_lis = len(lis)
for i in range(len(history) - 1, -1, -1):
    if len_lis < 0:
        break
    if len_lis == history[i]:
        arr[i][0] = -1
        len_lis = len_lis - 1

for a in arr:
    if a[0] != -1:
        print(a[0])