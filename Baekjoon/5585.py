'''
문제 링크: https://www.acmicpc.net/problem/5585
카테고리: 그리드
문제 해설: 거스름돈을 줄 때, 가장 적은 동전의 개수로 줄 수 있는 방법을 찾는 문제
'''
def main(a):
  a = 1000 - a
  coins = [500, 100, 50, 10, 5, 1]
  count = 0
  for coin in coins:
    count += a // coin
    a %= coin
  return count

print(main(int(input())))