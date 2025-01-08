'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/1644
카테고리
- 수학
- 정수론
- 두 포인터
- 소수 판정
- 에라토스테네스의 체

문제 해설
'''

import math

n = int(input())

def find_prime(n):
    prime_nums = [True] * (n + 1)
    ret = []

    for i in range(2, math.ceil(math.sqrt(n + 1))):
        if prime_nums[i]:
            for j in range(i * 2, n + 1, i):
                prime_nums[j] = False

    for i in range(2, n + 1):
        if prime_nums[i]:
            ret.append(i)

    return ret

prime_nums = find_prime(n)

print(prime_nums)

ret = 0
start = 0
end = 1

while start < n and end < n:
    sum_of_prime = sum(prime_nums[start:end + 1])
    if sum_of_prime == n:
        print(start , '~', end)
        print(*prime_nums[start:end + 1], sep=' ')
        print(sum_of_prime)
        ret = ret + 1
        start = start + 1
    elif sum_of_prime < n:
        end = end + 1
    else:
        start = start + 1

print()
print('result: ', end='')
print(ret)