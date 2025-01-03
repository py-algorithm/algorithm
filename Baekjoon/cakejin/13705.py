'''
작성자: cakejin
문제 링크: https://www.acmicpc.net/problem/13705
카테고리: 수학, 이분탐색, 임의 정밀도 / 큰 수 연산, 수치해석
문제 해설: Ax+Bsin(x)=C

A, B, C가 주어졌을 때, Ax+Bsin(x)=C를 만족하는 x를 찾는 프로그램을 작성
입력: 첫째 줄 정수 A, B, C
출력: 소수점 여섯째 자리까지 출력(반올림)

f(x)=Ax+Bsin(x)-C=0의 수치해 찾기
f'(x)=A+Bcos(x)

해가 존재하는 구간 모름: a1,b1사이에 존재한다 가정
                        (f(a1)f(b1) < 0 인 a1,b1찾기)
                        f(x): 증가함수 -> Ax+Bsin(x) 의 해는 0근방
                            f(x)의 해는 C근방

1.이분법 이용
    a1,b1사이에 근 존재-> cn=(an+bn)/2
    bn-cn <= 오차 -> break, cn이 수치해
    안끝나면: f(an)f(cn)<=0 ->an+1 = an, bn+1 = cn
                       >=0 ->an+1 = cn, bn+1 = b 
'''

import sys
import math

A, B, C = map(int, input().split())

#초기값 설정
a = C - 1
b = C + 1
c = (a + b)/2
er = 0.0000000001

def f(x):
    sin_x = math.sin(x)
    return A*x + B*sin_x - C

while f(a)*f(b) > 0:
    a -= 1
    b += 1

while b - c > er:
    fb = f(b)
    fc = f(c)

    if fb*fc <= 0: #fb가 양수, fc가 음수 -> a=c, b=b
        a = c
        c = (a + b)/2
    else: #fb,fc둘다 양수->a=a, b=c
        b = c
        c = (a + b)/2

print(round(c, 6))
        





