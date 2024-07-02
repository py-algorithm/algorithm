'''
문제 링크: https://www.acmicpc.net/problem/2588
카테고리: 수학
문제 해설: (세 자리 수) × (세 자리 수)
'''
a=int(input())
b=int(input())

i=a*(b%10)
j=a*(b%100-b%10)//10
k=a*(b-b%100)//100

print(i)
print(j)
print(k)
print(i+j*10+k*100)