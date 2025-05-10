/**
 * @author 99mini
 * @see https://www.acmicpc.net/problem/2206
 * @tag BFS, 그래프 탐색
 * @description
 */
function solution(n, m, grid) {
  /**
   * @description
   *    - [row, col, score, cnt]
   *    - score: 이동경로
   *    - cnt: 벽을 부순 횟수 0, 1
   * @type [number, number, number, number][]
   */
  const que = [];

  /**
   * @description queue head pointer
   * @type number
   */
  let ptr = 0;

  /**
   * @description
   * - 자바스크립트에서 큐가 없기 때문에 ptr을 이용하여 popLeft의 시간복잡도 O(1)보장
   * - 공간복잡도 비해결
   */
  const q = {
    data: que,
    popLeft: () => que[ptr++],
    /**
     * @type (v: typeof que[0]) => void
     */
    push: (v) => que.push(v),
  };

  q.push([0, 0, 1, 0]);

  /**
   * @description n by m by 2 3d array
   * @type number[][][]
   */
  const visited = Array.from({ length: n }, () =>
    Array.from({ length: m }, () => Array.from({ length: 2 }).fill(false))
  );

  const dn = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];

  while (q.data.length > ptr) {
    const [row, col, score, cnt] = q.popLeft();

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

      // if wall and broken count is 0.
      if (cell === "1" && cnt === 0) {
        q.push([nr, nc, score + 1, cnt + 1]);
        visited[nr][nc][cnt + 1] = true;
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
  const [N, M] = lines[0].map(Number);

  const grid = lines.slice(1).map((v) => String(v).split(""));

  console.log(solution(N, M, grid));

  process.exit(0);
});
