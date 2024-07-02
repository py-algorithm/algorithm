'''
문제 링크:https://www.acmicpc.net/problem/10852
카테고리:수학
문제해설:n개의 숫자 리스트의 최소, 최대 출력
'''

n=int(input())
m=list(map(int,input().split())) #한줄에 여러개 입력

print(min(m),max(m))

