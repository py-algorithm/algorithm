'''
문제 링크:https://www.acmicpc.net/problem/1181
카테고리: 문자열, 정렬
문제해설: 단어 정렬

n개의 단어 입력받음
단어 길이 짧은 순, 길이 같으면 사전 순으로 나열
중복된 단어는 하나만 남기고 삭제

sort & 집합

sys 사용시 개행문자도 출력->입력에 strip() 사용

'''
import sys

input = sys.stdin.readline

n = int(input())

arr = []

#입력받은 문자열 리스트에 담기
for _ in range(n):
  i = input().strip()
  arr.append(i)

arr=list(set(arr))
arr.sort()
arr.sort(key=len)

print(*arr, sep='\n')

  

