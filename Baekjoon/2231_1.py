'''
문제 링크:https://www.acmicpc.net/problem/2231
카테고리:브루트포스
문제해설:분해합의 생성자 구하기

M의 각자리수 + M

*523%10=3 append->(523-3)//10=52
->*52%10=2 append-> (52-2)//10=5=b
->if b<10->break

216입력->198출력
'''
N=int(input())

def M_sum(M):
  arr=[]

  while True:
    a=M%10
    arr.append(a)
    M=(M-a)//10
  
    if M<10:
      break

  return sum(arr)

for M in range(N+1):
  M_sum_all=M+M_sum(M)
  if M_sum_all==N:
    print(M)
    break
  else:
    print(0)