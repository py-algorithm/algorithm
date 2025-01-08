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
from decimal import Decimal, getcontext

# Decimal의 정밀도를 50자리까지 설정
getcontext().prec = 50

A, B, C = map(int, sys.stdin.readline().split())
A, B, C = Decimal(A), Decimal(B), Decimal(C)

#초기값 설정
#a = Decimal(-1)
#b = Decimal(1)
a = C / A - Decimal("1")
b = C / A + Decimal("1")

tol = Decimal("1e-7")

#def factorial1(n):
#    fac = 1
#    for i in range(2, n + 1):
#        fac *= i
#    return fac

def sin_meclaurin(x, terms = 20):
    x = Decimal(x)
    result = Decimal(0)
    term = x
    for n in range(1, terms + 1):
        result += term
        #term *= ((-1) ** n) * (x ** (2 * n +1)) / factorial1(2 * n  + 1)
        term *= -x**2 / (2 * n * (2 * n + 1))
        if abs(term) < tol:
            break
    return result



def f(x):
    #sin_x = math.sin(x)
    return A * x + B * sin_meclaurin(x) - C


while f(a)*f(b) > 0:
    a -= Decimal("1")
    b += Decimal("1")

while abs(b - a) > tol:
    c = ((a + b)/2) 
    fb = f(b)
    fc = f(c)

    if fb*fc <= 0: #fb가 양수, fc가 음수 -> a=c, b=b
        a = c
       
    else: #fb,fc둘다 양수->a=a, b=c
        b = c

print(f"{c:.6f}")



        





