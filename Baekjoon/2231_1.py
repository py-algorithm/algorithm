'''
문제 링크:https://www.acmicpc.net/problem/2231
카테고리:브루트포스
문제해설:분해합의 생성자 구하기
'''
n=int(input())

def func(m):
  arr=[]
  a=m%10
  arr.append(m)
  m=(m-a)%10
  print(arr)
  if m!=0:
    func(m)
  elif m==0:
    m=(m-a)//10
    arr.append(m)

for m in range(1,n+1):
  m_sum=m+sum(func(m))
  if m_sum==n:
    print(m)
    break
  else:
    print(0)
