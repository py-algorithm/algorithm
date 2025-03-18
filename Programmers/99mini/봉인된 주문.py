'''
작성자: 99mini
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/389481?language=python3
카테고리: 문자열
문제 해설: 
'''

test_case = [
    [30, ["d", "e", "bb", "aa", "ae"], "ah"],
    [7388, ["gqk", "kdn", "jxj", "jxi", "fug", "jxg", "ewq", "len", "bhc"], "jxk"],
]

def solution(n, bans):
    
    unit = ord('z') - ord('a') + 1
    
    def alpha_of(val):
        curr = val
        ret = ''
        while curr > 0:
            remain = curr % unit
            
            ret += chr(remain + ord('a') - 1)
            curr //= unit
        
        return ret[::-1]
            
    removed = 0
    
    for ban in sorted(bans, key=lambda x: (len(x), x)):
        alpha = 0
        for idx, b in enumerate(ban[::-1]):
            alpha += ((ord(b) - ord('a') + 1)) * unit ** idx
        if alpha <= n + removed:
            removed += 1
    
    return alpha_of(n + removed)

for test in test_case:
    n, bans, result = test
    print(sorted(bans, key=lambda x: (len(x), x)))
    ret = solution(n, bans)

    print(f"expected result: {result}")
    print(f"solution result: {ret}")
    if ret == result:
        print("Success")
    else:
        print("Fail")