'''
작성자: 99mini
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181188
카테고리: 정렬
문제해설: 
'''

def solution(targets):
    answer = 0
    
    targets.sort(key=lambda x: x[1])
    
    prev = -1
    
    for target in targets:
        # 요소의 시작점과 이전 발사 지점 비교
        if target[0] > prev:
            answer += 1
            # 이전 발사 지점을 요소의 끝점 - 0.5로 초기화
            prev = target[-1] - 0.5
    
    return answer

test_case = [
    (
        [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]],
        3
    )
]

for test in test_case:
    targets, expected = test

    result = solution(targets)

    print(f"result: {result}\nexpected: {expected}")
    if result == expected:
        print("Success")
    else:
        print("Fail")

