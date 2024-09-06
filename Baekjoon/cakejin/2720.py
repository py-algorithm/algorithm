'''
문제링크:https://www.acmicpc.net/problem/2720
카테고리:그리디
문제 해설: 거스름돈 각각 개수 구하기
쿼터(Quarter, $0.25)의 개수, 다임(Dime, $0.10)의 개수, 니켈(Nickel, $0.05)의 개수, 페니(Penny, $0.01)
'''
t=int(input())

for i in range(t):
  a=int(input())
  coins=[25,10,5,1]
  count=[0,0,0,0]
  for index, coin in enumerate(coins):
    count[index] += a//coin
    a%=coin
  print(*count, sep=' ')
