'''
작성자: 99mini
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/340211
카테고리: 구현
문제 해설: TODO: WIP
'''

test_case = [
    [
        ["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"],
        ["13 - 6 = 5"]
    ],
    [
        ["1 + 1 = 2", "1 + 3 = 4", "1 + 5 = X", "1 + 2 = X"],
        ["1 + 5 = ?", "1 + 2 = 3"]
    ],
    [
        ["10 - 2 = X", "30 + 31 = 101", "3 + 3 = X", "33 + 33 = X"],
        ["10 - 2 = 4", "3 + 3 = 10", "33 + 33 = 110"]
    ],
    [
        ["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "5 - 5 = X"],
        ["2 + 2 = 4", "7 + 4 = ?", "5 - 5 = 0"]
    ],
    [
        ["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "8 + 4 = X"],
        ["2 + 2 = 4", "7 + 4 = 12", "8 + 4 = 13"]
    ],
]

def solution(expressions):
    answer = []
    return answer

for test in test_case:
    expressions, result = test
    ret = solution(expressions)

    print(f"expected result: {result}")
    print(f"solution result: {ret}")
    if ret == result:
        print("Success")
    else:
        print("Fail")