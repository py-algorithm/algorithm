'''
작성자: 99mini
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/172927
카테고리: 구현, 정렬
문제해설: 
'''

def solution(picks, minerals):
    answer = 0
    n = len(minerals)
    
    minerals_range = []
    
    for i in range(0, n, 5):
        dia     = 0
        iron    = 0
        stone   = 0
        
        for j in range(i, min(i + 5, n)):
            if minerals[j] == "diamond":
                dia += 1
            elif minerals[j] == "iron":
                iron += 1
            else:
                stone += 1
                
        minerals_range.append((dia, iron, stone))
    
    minerals_range = minerals_range[:sum(picks)]
    minerals_range.sort(key=lambda x: (-x[0], -x[1], -x[2]))

    for m in minerals_range:
        m_len = sum(m)

        if picks[0]:
            answer += m_len
            picks[0] -= 1
        elif picks[1]:
            dia_cnt = m[0]
            
            answer += (dia_cnt * 5 + m_len - dia_cnt)
            picks[1] -= 1
        elif picks[2]:
            dia_cnt = m[0]
            iron_cnt = m[1]

            answer += (dia_cnt * 25 + iron_cnt * 5 + m_len - dia_cnt - iron_cnt)
            picks[2] -= 1
        else:
            break
                
        
    return answer

test_case = [
    (
        [1, 3, 2],
        ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"],
        12
    ),
    (
        [0, 1, 1],
        ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"],
        50
    ),
    (
        [0, 0, 1],
        ["stone", "diamond", "diamond", "diamond", "diamond", "diamond"],
        101
    ),
    (
        [0, 0, 1],
        ["stone", "stone", "stone", "stone", "stone", "diamond"],
        5
    )
]

for test in test_case:
    picks, minerals, expected = test

    result = solution(picks, minerals)

    print(f"result: {result}\nexpected: {expected}")
    if result == expected:
        print("Success")
    else:
        print("Fail")