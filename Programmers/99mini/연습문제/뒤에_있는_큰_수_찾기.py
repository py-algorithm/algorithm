'''
작성자: 99mini
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/154539
카테고리: 스택
문제해설: 
'''

def solution(numbers):
    answer = [-1]
    stack = [numbers[-1]]
    
    n = len(numbers)
    
    for i in range(n - 2, -1, -1):
        while stack:
            if stack[-1] <= numbers[i]:
                stack.pop()
            else:
                answer.append(stack[-1])
                break
        if not stack:
            answer.append(-1)
            
        stack.append(numbers[i])
    
    return answer[::-1]