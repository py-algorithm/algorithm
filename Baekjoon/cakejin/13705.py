'''
작성자: cakejin
문제 링크: https://www.acmicpc.net/problem/13705
카테고리: 수학, 이분탐색, 임의 정밀도 / 큰 수 연산, 수치해석
문제 해설: Ax+Bsin(x)=C

A, B, C가 주어졌을 때, Ax+Bsin(x)=C를 만족하는 x를 찾는 프로그램을 작성
입력: 첫째 줄 정수 A, B, C
출력: 소수점 여섯째 자리까지 출력(반올림)

f(x)=Ax+Bsin(x)-C=0의 수치해 찾기

해가 존재하는 구간 모름: a1,b1사이에 존재한다 가정
                        (f(a1)f(b1) < 0 인 a1,b1찾기)
                        f(x): 증가함수

이분법 이용
    a1,b1사이에 근 존재-> cn=(an+bn)/2
    bn-an <= 오차 -> break, cn이 수치해
    안끝나면: f(an)f(cn)<=0 ->an+1 = an, bn+1 = cn
                       >=0 ->an+1 = cn, bn+1 = b 
소수의 정확한 연산
-부동 소수점 말고 고정 소수점 이용: Decimal
'''

import sys
import decimal

# Decimal의 정밀도를 100자리까지 설정
decimal.getcontext().prec = 100
decimal.getcontext().rounding = decimal.ROUND_HALF_UP

A, B, C = map(int, sys.stdin.readline().split())
A, B, C = decimal.Decimal(A), decimal.Decimal(B), decimal.Decimal(C)

#초기값 설정
#-1<sin<1
a = decimal.Decimal("0")
b = decimal.Decimal("10")

tol = decimal.Decimal("1e-20")

def sin_meclaurin(x, terms = 25):
    result = decimal.Decimal(0)
    #x범위를 -2pi~2pi로 축소
    pi = decimal.Decimal('3.141592653589793238462643383279502884197169399375105820974944592307816406286')
    two_pi = decimal.Decimal('2') * pi
    x = x % two_pi
    term = x
    for n in range(1, terms + 1):
        result += term
        #term *= ((-1) ** n) * (x ** (2 * n +1)) / factorial(2 * n  + 1)
        term *= decimal.Decimal(-x ** 2) / (decimal.Decimal(2 * n) * decimal.Decimal(2 * n + 1))
        if abs(term) < tol:
            break
    return result



def f(x):
    return A * x + B * sin_meclaurin(x) - C


while f(a)*f(b) > 0:
    a -= decimal.Decimal("1")
    b += decimal.Decimal("1")

while abs(b - a) > tol:
    c = (a + b)/2 
    fa = f(a)
    fc = f(c)

    if abs(fc) <= tol:
        break
    elif fa * fc > 0:
        a = c
 
    else: 
        b = c

print(round(c, 6))



        





