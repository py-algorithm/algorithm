'''
문제 링크:https://www.acmicpc.net/problem/2798
카테고리: 브루트포스 알고리즘
문제해설: 블랙잭
'''
import itertools

n,m=map(int,input().split())
cards=list(map(int,input().split()))

#카드 n개중 3장의 합이 m을 넘지 않지만 가장 가깝게
#경우의수 nC3
nCr=list(itertools.combinations(cards,3))
a=len(nCr)
result=0

for comb in nCr:
  sum_comb=sum(comb)
  if sum_comb<=m:  
    result=max(sum_comb,result)

    if result==m:
      break
print(result)
