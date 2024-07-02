#1.소수판별_x의제곱근까지만 보면된다
import math

'''def prime_num(x):
  for i in range (2,int(math.sqrt(x)+1)):
    if x%i==0:
      return False
    return True
print(prime_num(4))
print(prime_num(7))'''

#에라토스테네스의체
n=int(input())
arr=[True for i in range(n)]

for i in range(2,int(math.sqrt(n)+1)):
  if arr[i]==True:
    for j in range(2,n):
      arr[i*j]==False

print(i)