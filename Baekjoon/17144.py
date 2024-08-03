'''
문제 링크: https://www.acmicpc.net/problem/17144
카테고리: 구현, 시뮬레이션
문제 해설


1. 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
- (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
- 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
- 확산되는 양은 Ar,c/5이고 소수점은 버린다. 즉, ⌊A_(r,c) / 5⌋이다.
- (r, c)에 남은 미세먼지의 양은 A_(r, c) - ⌊A_(r, c) / 5⌋ x (확산된 방향의 개수) 이다.

2. 공기청정기가 작동한다.
- 공기청정기에서는 바람이 나온다.
- 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
- 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
- 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.
'''

class Room:
  def __init__(self, metrix: list[list[int]]):
    self.room = metrix

  def spread(self):
    pass

  def getTotalDust() -> int:
    pass

class Cleaner:

  def __init__(self, r: int, c: int):
    self.r = r
    self.c = c

  def work(self, room: Room):

    return
  

  
def main():
  r, c, t = map(int, input().split())
  metrix = list(list(map(int, input().split())) for _ in range(r))

  room = Room(metrix)
  cleaner = Cleaner(r, c)

  for _ in range(t):
    room.spread()
    cleaner.work(room)

  print(room.getTotalDust())

main()