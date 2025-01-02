'''
문제 링크:https://www.acmicpc.net/problem/4949
카테고리: 자료 구조, 문자열, 스택
문제해설: 균형잡힌 세상

(),[]가 균형이루기 + 괄호 안 괄호도 균형
주어진 문자열이 균형인지 판단

스택에 ([나올때마다 쌓아두다가)]나오면 마지막에 쌓은 두개 빼기->끝까지 했을때 스택에 남아있는게 없으면 yes
'''

import sys

while True:
  
  input_string = sys.stdin.readline().rstrip()
  
  if input_string == ".":
    break
  
  a = len(input_string)
  stack = []
  balance = True


  for i in range(a):
    if input_string [i] == '(' or input_string[i] == '[':
      stack.append(input_string[i])
      
    elif input_string[i] == ')':
      if not stack or stack[-1] != '(':
        balance = False
        break
      stack.pop()

    elif input_string[i] == ']':
      if not stack or stack[-1] != '[':
        balance = False
        break
      stack.pop()

  if balance and not stack:
    print("yes")

  else:
    print("no")
  
