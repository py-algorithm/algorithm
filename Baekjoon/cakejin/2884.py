'''
문제 링크: https://www.acmicpc.net/problem/2884
카테고리: 수학
문제 해설: 설정한 시간 보다 45분 빠른 시간 출력하기.
'''

h,m=map(int,input().split())

if m<45 and 0<h:
 print(h-1,m+15)
elif m<45 and h==0:
  print(23,m+15)
else:
  print(h,m-45)