'''
문제 링크:https://www.acmicpc.net/problem/2231
카테고리:브루트포스
문제해설:분해합의 생성자 구하기
'''
n=int(input())

#n=m+m//100+(m-m//100)//10+(m-m//100-..)->resursive?

#찾은m을 재귀적으로 n에 넣기

#m을 1부터n까지 완전탐색으로 찾기
for m in range(1,n+1):
  a=sum(map(int,str(m)))
  m_sum=m+a 
  '''m_sum말고 sum을 했더니 
  'int' object is not callable오류발생'''
  if m_sum==n:
    print(m)
    break #break없으면 모든 생성자 출력함
else:
  print(0)
  