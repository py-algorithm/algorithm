'''
작성자: 99mini
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

import math

class Room:

  dr = [0, 0, 1, -1]
  dc = [1, -1, 0 ,0]

  def __init__(self, metrix: list[list[int]]) -> None:
    self.r = len(metrix)
    self.c = len(metrix[0])
    self.room = metrix

    cleaner_position_top = 0

    for row in range(self.r):
      if metrix[row][0] == -1:
        cleaner_position_top = row
        break

    self.cleaner = Cleaner(cleaner_position_top)

  def spread(self) -> None:
    diff_room = [[0 for _ in range(self.c)] for _ in range(self.r)]

    for row in range(self.r):
      for col in range(self.c):
        
        if self.room[row][col] < 1:
          continue

        spread_amount = math.floor(self.room[row][col] / 5)

        spread_count = 0
        for r, c in zip(self.dr, self.dc):
          nr = row + r
          nc = col + c

          if self.is_bound(nr, nc):
            spread_count += 1
            diff_room[nr][nc] += spread_amount

        diff_room[row][col] -= spread_count * spread_amount
    
    new_room = []

    for old_row, diff_row in (zip(self.room, diff_room)):  
      new_room.append([x + y for x, y in zip(old_row, diff_row)])

    self.room = new_room

  def is_bound(self, r: int, c: int) -> bool:
    if c == 0 and (self.cleaner.top == r or self.cleaner.bottom == r):
      return False
    
    return self.r > r and r >= 0 and self.c > c and c >=0

  def getTotalDust(self) -> int:
    return sum(sum(self.room, [])) + 2

class Cleaner:

  def __init__(self, position_top: int):
    self.top = position_top
    self.bottom = position_top + 1

  def work(self, room: Room):
    r = len(room.room)

    top_right_end = room.room[self.top][-1]
    top_right_start = room.room[0][-1]

    top_left_start = room.room[0][0]

    self.__shift_row(room, self.top)
    self.__shift_row(room, 0, top_right_start)

    for i in range(self.top):
      new_value = room.room[i + 1][-1]
      if i == self.top -1 :
        new_value = top_right_end

      room.room[i][-1] = new_value

    for i in reversed(range(1, self.top)):
      new_value = room.room[i - 1][0]
      if i == 1:
        new_value = top_left_start
      room.room[i][0] = new_value
      
    bottom_right_end = room.room[self.bottom][-1]
    bottom_right_start = room.room[-1][-1]

    bottom_left_end = room.room[-1][0]

    self.__shift_row(room, self.bottom)
    self.__shift_row(room, -1, bottom_right_start)

    for i in reversed(range(self.bottom + 1, r)):
      new_value = room.room[i - 1][-1]
      if i == self.bottom + 1:
        new_value = bottom_right_end
      room.room[i][-1] = new_value

    for i in range(self.bottom + 1, r - 1):
      new_value = room.room[i + 1][0]
      if i == r - 2:
        new_value = bottom_left_end
      room.room[i][0] = new_value
  
  def __shift_row(self, room: Room, row: int, first_value: int | None = None):
    if first_value == None:
      room.room[row][1:] = [0] + room.room[row][1:-1]
    else:
      room.room[row] = room.room[row][1:] + [first_value]
  
def main():
  r, c, t = map(int, input().split())
  metrix = list(list(map(int, input().split())) for _ in range(r))

  room = Room(metrix)

  for _ in range(t):
    room.spread()
    room.cleaner.work(room)

  print(room.getTotalDust())

main()