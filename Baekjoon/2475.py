'''
문제 링크:https://www.acmicpc.net/problem/2475
카테고리:수학, 구현, 사칙연산
문제해설:주어진 조건대로 연산된 검증수 출력하기
'''
a,b,c,d,e=map(int,input().split())
i=(a*a+b*b+c*c+d*d+e*e)%10
print(i)
