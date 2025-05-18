/**
 * @author @99mini
 * @see https://www.acmicpc.net/problem/16933
 * @tag BFS, 그래프 탐색
 * @description
 */
function solution(n, m, k, grid) {
  class Queue {
    constructor() {
      this.head = null;
      this.tail = null;
      this.length = 0;
    }
    push(val) {
      const newItem = { data: val, next: null };
      if (this.head === null) {
        this.head = newItem;
      } else {
        this.tail.next = newItem;
      }
      this.tail = newItem;
      this.length++;
    }
    popLeft() {
      const val = this.head.data;
      this.head = this.head.next;
      this.length--;
      return val;
    }
  }
  const q = new Queue();

  q.push([0, 0, 1, 0]);

  /**
   * @description n by m by k 3d array
   * @type boolean[][][]
   */
  const visited = Array.from({ length: n }, () =>
    Array.from({ length: m }, () => Array.from({ length: k }).fill(false))
  );

  const dn = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];

  while (q.length) {
    const [row, col, score, cnt] = q.popLeft();
    const isDay = score % 2 === 1;

    if (row === n - 1 && col === m - 1) {
      return score;
    }

    for (const [dr, dc] of dn) {
      const nr = dr + row;
      const nc = dc + col;

      // out of boundary
      if (0 > nr || nr >= n || 0 > nc || nc >= m) {
        continue;
      }

      // visited
      if (visited[nr][nc][cnt]) {
        continue;
      }

      const cell = grid[nr][nc];

      // if wall and broken count is less than k
      if (cell === "1" && cnt < k) {
        // is day
        // break wall
        if (isDay) {
          q.push([nr, nc, score + 1, cnt + 1]);
          visited[nr][nc][cnt + 1] = true;
        }
        // is not day
        // keep here and add score
        else {
          q.push([row, col, score + 1, cnt]);
        }
      }
      // if is not wall
      else if (cell === "0") {
        q.push([nr, nc, score + 1, cnt]);
        visited[nr][nc][cnt] = true;
      }
    }
  }

  return -1;
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  prompt: "OHAI> ",
});

const lines = [];

rl.on("line", (line) => {
  /** 입력 받는 영역 */
  lines.push(line.split(" "));
}).on("close", () => {
  /** 문제 해결 영역 */
  const [N, M, K] = lines[0].map(Number);

  const grid = lines.slice(1).map((v) => String(v).split(""));

  console.log(solution(N, M, K, grid));

  process.exit(0);
});
