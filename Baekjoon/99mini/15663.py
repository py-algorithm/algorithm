'''
작성자: 99mmini
문제 링크: https://www.acmicpc.net/problem/15663
카테고리: 백트레킹
문제 해설:
백트레킹으로 순열 생성

- 중복된 숫자을 경우 `저장해 둔 데이터`(`check`)와 `현재 순환에서 요소`(`nums[i]`)와 비교
- for i in range(n) 을 순회하기 때문에 방문 기록(`visited`)를 전역으로 관리. 
    - 한 요소의 back tracking이 끝났을 경우 방문 기록 해지(False)

'''

def back():
    check = 0
    if len(answer) == m:
        print(*answer)
        return
    for i in range(n):
        if check != num[i] and not visited[i]:
            answer.append(num[i])
            visited[i] = True
            check = num[i]
            back()
            answer.pop()
            visited[i] = False

n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
visited = [False] * n
answer = []

back()