'''
문제 링크:https://www.acmicpc.net/problem/4153
카테고리:수학, 기하학, 피타고라스 정리
문제해설:직각삼각형 판별
'''
while True:
  a,b,c=map(int,input().split())

  if a==0 and b==0 and c==0:
    break
  

  if a**2+b**2==c**2 or b**2+c**2==a**2 or a**2+c**2==b**2:
    print('right')
  else:
    print('wrong')
