'''
문제 링크:https://www.acmicpc.net/problem/2751
카테고리: 정렬
문제해설: 수 정렬하기2

선택정렬n^2
퀵정렬nlogn->메모리초과!
계수정렬n->동인한 값 반복 등장시 효율적

'''

import sys
import random

input=sys.stdin.readline

n=int(input())

m=[int(input()) for _ in range(n)]

def quick_sort(array):
  if len(array) <= 1:
    return array
  
  #pivot을 첫번째원소로 고정시 최악의 경우 시간 복잡도 n^2
  pivot = random.choice(array)

  left_side = [x for x in array if x <= pivot]
  right_side = [x for x in array if x > pivot]

  return quick_sort(left_side) + quick_sort(right_side)
  
print(*quick_sort(m), sep='\n')





