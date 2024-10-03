'''
문제 링크:https://www.acmicpc.net/problem/2164
카테고리:자료 구조, 큐
문제해설:카드2

1
2
.
.
n
순서의 카드
최상단 카드 버리기->최상단카드를 제일 아래로 옮기기-
->카드 한장 남을 때 까지 반복
ex)1234->234->342->42->24->4

큐:선입선출
1~n까지 리스트에 담기
'최상단제거->그다음최상단 맨밑'반복 until 리스트 원소 1개

반복문: for이용 시 리스트 초기값이 계속 변함->while 사용하기
'''
import sys
from collections import deque

input = sys.stdin.readline()

n = int(input)

dq = deque(list(i for i in range(1, n+1)))

while len(dq) > 1:
  
  dq.popleft()
  dq.append(dq.popleft())
    

print(dq[0])

