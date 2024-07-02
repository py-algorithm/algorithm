'''
문제 링크:https://www.acmicpc.net/problem/10952
카테고리:수학
문제해설:n개의 줄로 입력된 두 정수 더한 값을 한줄씩 출력
'''

while True:
  a,b=map(int,input().split())
  if a==0 and b==0: #예제 입력에 0 0 입력시 출력에 안보임
    break
  else:
    print(a+b, sep='\n')
