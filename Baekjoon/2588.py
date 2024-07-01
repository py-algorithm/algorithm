'''
문제 링크: https://www.acmicpc.net/problem/2588
카테고리: 수학
문제 해설: (세 자리 수) × (세 자리 수)
'''
a=int(input())
b=int(input())

arr=[a*(b%10),
     a*(b%100-b%10),
     a*(b-b%100),
     a*(b%10)+a*(b%100-b%10)+a*(b-b%100)]

print(arr[0])
print(arr[1]//10)
print(arr[2]//100)
print(arr[3])