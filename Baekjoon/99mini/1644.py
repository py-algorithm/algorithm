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
1. `find_prime_suffix`: 에라토스테네스의 체를 이용하여 소수 판별 후 소수의 누적합 반환
2. 투 포인터로 start(=0)와 end(=1)를 사용.
    - 누적합(start ~ end)의 값이 목표값(n)과 같으면 결과값 +1
    - 누적합의 값이 목표값보다 작으면 end값 +1
    - 그렇지 않은 경우 start값 +1
    - start와 end값이 소수의 누적합 배열의 길이보다 작을 때까지 반복 
'''

import math

n = int(input())

def find_prime_suffix(n):
    if n < 2:
        return []

    prime_nums = [True] * (n + 1)
    ret = [2]

    for i in range(2, math.ceil(math.sqrt(n + 1))):
        if prime_nums[i]:
            for j in range(i * 2, n + 1, i):
                prime_nums[j] = False

    for i in range(2, n + 1):
        if prime_nums[i]:
            ret.append(ret[-1] + i)

    return ret

prime_num_suffix = find_prime_suffix(n)

ret = 0

len_of_prime_num_suffix = len(prime_num_suffix)

start = 0
end = 1

while start < len_of_prime_num_suffix and end < len_of_prime_num_suffix:
    sum_of_prime = prime_num_suffix[end] - prime_num_suffix[start]
    if sum_of_prime == n:
        ret = ret + 1
        start = start + 1
    elif sum_of_prime < n:
        end = end + 1
    else:
        start = start + 1

print(ret)