'''
문제 링크: https://www.acmicpc.net/problem/5585
카테고리: 그리디 알고리즘
문제 해설: 기본 거스름돈 구하기
'''
def main(a):
    a=1000-a
    coin=[500,100,50,10,5,1]
    count=0
    for i in coin:
        count+=a//i
        a%=i
    return count

print(main(int(input())))