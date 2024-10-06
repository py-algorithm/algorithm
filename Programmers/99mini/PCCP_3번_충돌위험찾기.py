'''
작성자: 99mmini
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/340211
카테고리: 구현
문제 해설: 
'''

test_case = [
    [
        [[3, 2], [6, 4], [4, 7], [1, 4]],
        [[4, 2], [1, 3], [2, 4]],
        1
    ],
    [
        [[3, 2], [6, 4], [4, 7], [1, 4]],
        [[4, 2], [1, 3], [4, 2], [4, 3]],
        9
    ],
    [
        [[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]],	
        [[2, 3, 4, 5], [1, 3, 4, 5]],	
        0
    ],
]

def solution(points, routes):
    answer = 0

    robot_paths = []

    for route in routes:
        robot_path = [points[route[0] - 1]]
        
        for path in route[1:]:
            start_point = robot_path[-1]
            destination = points[path - 1]

            # row 비교
            while robot_path[-1][0] != destination[0]:
                # 출발지가 더 큰 경우
                if start_point[0] > destination[0]:
                    robot_path.append([robot_path[-1][0] - 1, robot_path[-1][1]])
                
                elif start_point[0] < destination[0]:
                    robot_path.append([robot_path[-1][0] + 1, robot_path[-1][1]])

            # col 비교
            while robot_path[-1][1] != destination[1]:
                # 출발지가 더 큰 경우
                if start_point[1] > destination[1]:
                    robot_path.append([robot_path[-1][0], robot_path[-1][1] - 1])
                
                elif start_point[1] < destination[1]:
                    robot_path.append([robot_path[-1][0], robot_path[-1][1] + 1])
            
        robot_paths.append(robot_path)

    for i in range(max(map(len, robot_paths))):

        curr = dict()
        x = len(robot_paths)

        for j in range(x):
            if i < len(robot_paths[j]):
                value = tuple(robot_paths[j][i])

                curr[value] = value in curr.keys()
        answer += sum(curr.values())

    return answer


for test in test_case:
    points, routes, result = test
    ret = solution(points, routes)

    print(f"expected result: {result}")
    print(f"solution result: {ret}")
    if ret == result:
        print("Success")
    else:
        print("Fail")