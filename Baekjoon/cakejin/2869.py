'''
문제 링크:https://www.acmicpc.net/problem/2869
카테고리: 수학
문제해설: 달팽이는 올라가고 싶다

하루 올라간 높이=a-b
다음날 올라간 높이=(a-b)+a-b
...
정상 도달 후 끝
'''
import math

a,b,v=map(int,input().split())

'''
v=(d)*a-(d-1)*b
v=d*(a-b)+b
(v-b)/(a-b)=d
'''
print(math.ceil((v-b)/(a-b)))

