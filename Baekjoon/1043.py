'''
문제 링크:https://www.acmicpc.net/problem/1043
카테고리: 자료 구조, 그래프 이론, 그래프 탐색, 분리 집합
문제해설

1. 양방향 그래프 초기화 (`dict` 사용)
2. 진실을 알고 있는 사람과 연결된 사람을 `known_members: set[int]`에 업데이트
3. 파티의 멤버와 진실을 알고 있는 멤버 비교
  3.1. (파티의 멤버)와 (진실을 알고 있는 멤버)가 같은 경우 -> 다음 파티의 멤버 검사
  3.2. (파티의 멤버)보다 (진실을 알고 있는 멤버)가 큰 경우 -> 과장된 이야기를 할 수 있음
  3.3. (파티의 멤버)보다 (진실을 알고 있는 멤버의 최대값)가 작은 경우 -> 과장된 이야기를 할 수 있음

> 파티의 멤버와 진실을 알고 있는 멤버는 오름차순으로 정렬되어 있다.
'''

n, m = map(int, input().split())

truth_members = list(map(int, input().split()))[1:]

parties: list[list[int]] = []
graph: dict[int, list[int]] = dict([])

for _ in range(m):
  party = sorted(list(map(int, input().split()))[1:])
  parties.append(party)

  for member in party:
    graph[member] = set(list(graph.get(member, [])) + party)

known_members = set(truth_members.copy())

for t in truth_members:
  known_members.update(list(graph.get(t, [])))

known_members_sorted = sorted(list(known_members))

result = 0

for party in parties:
  is_valid = True
  for member in party:
    for known_member in known_members_sorted:
      if member == known_member:
        is_valid = False
        break
      if member < known_member:
        break
    if not is_valid:
      break
  if is_valid:
    result += 1

print(result)