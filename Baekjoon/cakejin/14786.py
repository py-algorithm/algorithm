'''
작성자: cakejin
문제 링크: https://www.acmicpc.net/problem/14786
카테고리: 수학, 이분탐색, 수치해석
문제 해설: Ax+Bsin(x)=C (2)

A, B, C가 주어졌을 때, Ax+Bsin(x)=C를 만족하는 x를 찾는 프로그램을 작성
입력: 첫째 줄 정수 A, B, C

f(x)=Ax+Bsin(x)-C=0의 수치해 찾기

해가 존재하는 구간 모름: a1,b1사이에 존재한다 가정
                        (f(a1)f(b1) < 0 인 a1,b1찾기)
                        f(x): 증가함수
        
(절대, 상대 오차 10^-9까지 허용)

1.이분법 이용
    a1,b1사이에 근 존재-> cn=(an+bn)/2
    bn-an <= 오차 -> break, cn이 수치해
    안끝나면: f(an)f(cn)<=0 ->an+1 = an, bn+1 = cn
                       >=0 ->an+1 = cn, bn+1 = b 


예제
-입력: 1 1 20
-출력:19.4417867100477812106
'''

import sys
from math import sin


A, B, C = map(int, input().split())

#초기값 설정
a = - C
b = + C

tol = 1e-9

def f(x):
    return A * x + B * sin(x) - C


while f(a)*f(b) > 0:
    a -= 0.5
    b += 0.5


while b - a > tol:
    c = (a + b) / 2

    if f(c) > 0: #fc둘다 양수->a=a, b=c
        b = c
    else: #fc가 음수 -> a=c, b=b 
        a = c

print(c)
        





