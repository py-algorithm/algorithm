'''
문제 링크:https://www.acmicpc.net/problem/11050
카테고리: 수학, 구현, 조합론
문제해설: 이항 계수 1
nCk=n!/k!(n-k)!
'''
n,k=map(int,input().split())
result_n=1
result_nk=1
result_k=1

for i in range(2,n+1):
    result_n*=i
    if i <= k:
        result_k*=i
    if i <= n-k:
        result_nk*=i

result=result_n//(result_k*result_nk)
print(result)

