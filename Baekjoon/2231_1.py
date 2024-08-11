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

def m_sum(M):
  ret=M

  while M>0:
    ret += M%10
    M //= 10
  
  return ret



def result_M(N):
  
  for M in range(N+1):

    if m_sum(M)==N:
      return M
    
  return 0

print(result_M(N))