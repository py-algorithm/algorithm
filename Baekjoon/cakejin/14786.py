'''
작성자: cakejin
문제 링크: https://www.acmicpc.net/problem/14786
카테고리: 수학, 이분탐색, 수치해석
문제 해설: Ax+Bsin(x)=C (2)

A, B, C가 주어졌을 때, Ax+Bsin(x)=C를 만족하는 x를 찾는 프로그램을 작성
입력: 첫째 줄 정수 A, B, C

f(x)=Ax+Bsin(x)-C=0의 수치해 찾기
f'(x)=A+Bcos(x)

해가 존재하는 구간 모름: a1,b1사이에 존재한다 가정
                        (f(a1)f(b1) < 0 인 a1,b1찾기)
                        f(x): 증가함수 -> Ax+Bsin(x) 의 해는 0근방
                            f(x)의 해는 C근방
(절대, 상대 오차 10^-9까지 허용)
절대오차 = 참값 - 근사값
상대오차 = (참값-근사값)/참값

1.이분법 이용
    a1,b1사이에 근 존재-> cn=(an+bn)/2
    bn-cn <= 오차 -> break, cn이 수치해
    안끝나면: f(an)f(cn)<=0 ->an+1 = an, bn+1 = cn
                       >=0 ->an+1 = cn, bn+1 = b 
'''

import sys
import math
from decimal import Decimal, getcontext

getcontext().prec = 50

A, B, C = map(int, input().split())


#초기값 설정
a = Decimal(C - 1)
b = Decimal(C + 1)
c = Decimal((a + b)/2)
er = Decimal("1e-9")

def f(x):
    sin_x = math.sin(float(x))
    return A*x + B*Decimal(sin_x) - C


while f(a)*f(b) > 0:
    a -= 1 #Decimal(a-1)
    b += 1 #Decimal(b+1)

while b - a > er:
    fb = f(b)
    fc = f(c)

    if fb*fc <= 0: #fb가 양수, fc가 음수 -> a=c, b=b
        a = Decimal(c)
        c = Decimal((a + b)/2)
    else: #fb,fc둘다 양수->a=a, b=c
        b = Decimal(c)
        c = Decimal((a + b)/2)

print(c)
        





