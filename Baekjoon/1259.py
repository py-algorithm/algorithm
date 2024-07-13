'''
문제 링크:https://www.acmicpc.net/problem/1259
카테고리:구현, 문자열
문제해설:팰린드롬수 판별
'''
while True:
  a=input()
  n=len(a)

  flag=True

  if int(a)==0:
    exit(0)

  for i in range(n//2):
    if a[i]==a[n-1-i]:
      
      continue
    elif a[i]!=a[n-1-i]:
      print('no')
      flag=False
      break
  if flag:
    print('yes')

