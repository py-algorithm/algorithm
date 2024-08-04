'''
문제 링크:https://www.acmicpc.net/problem/15829
카테고리: 구현, 문자열, 해싱
문제해설: Hashing
'''
L=int(input())
l=list(input())
#h=(sigma(ai*r**i))*mod(M) ->r=31, M=1234567891
#아스키코드 a=97
M=1234567891
r=31
h=0

for i in range(L):
  a=ord(l[i])-96
  
  h+=a*r**i
  result=h%M
  
print(result)
