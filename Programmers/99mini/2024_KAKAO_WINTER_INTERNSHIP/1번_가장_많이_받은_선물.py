'''
작성자: 99mmini
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/258712
카테고리: 행렬, 해쉬 테이블
문제 해설:

참고
다른 사람의 풀이: https://school.programmers.co.kr/learn/courses/30/lessons/258712/solution_groups?language=python3
'''

def solution(friends, gifts):
    n = len(friends)
    
    answer = [0] * n
    
    table = [[0] * n for _ in range(n)]
    history = dict()
    
    for i, f in enumerate(friends):
        history[f] = dict({
            "given": 0,
            "received": 0,
            "gift_index": 0,
            "reward": 0,
            "table_index": i
        })
    
    for g in gifts:
        a, b = map(str, g.split(" "))
        
        given_f     = history[a]
        received_f  = history[b]
        
        given_index     = given_f["table_index"]
        received_index  = received_f["table_index"]
        
        table[given_index][received_index] += 1
        
        given_f["given"] += 1
        received_f["received"] += 1

    for h in history:
        history[h]["gift_index"] = history[h]["given"] - history[h]["received"]

    for i in range(n):
        for j in range(i + 1, n):
            if table[i][j] > table[j][i]:
                answer[history[friends[i]]["table_index"]] += 1
            elif table[i][j] < table[j][i]:
                answer[history[friends[j]]["table_index"]] += 1
            else:
                if history[friends[i]]["gift_index"] > history[friends[j]]["gift_index"]:
                    answer[history[friends[i]]["table_index"]] += 1
                elif history[friends[i]]["gift_index"] < history[friends[j]]["gift_index"]:
                    answer[history[friends[j]]["table_index"]] += 1

    return max(answer)