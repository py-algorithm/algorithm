/**
 * @author 99mini
 * @see https://www.acmicpc.net/problem/16933
 * @tag BFS, 그래프 탐색
 * @description
 */
function solution(n, m, k, grid) {
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

  const COMPACTION_THRESHOLD = 10_000;

  /**
   * @description
   * - 자바스크립트에서 큐가 없기 때문에 ptr을 이용하여 popLeft의 시간복잡도 O(1)보장
   * - 공간복잡도 비해결
   */
  const q = {
    data: que,
    popLeft: () => {
      const ret = que[ptr++];
      return ret;
    },
    /**
     * @type (v: typeof que[0]) => void
     */
    push: (v) => que.push(v),
  };

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

  while (q.data.length > ptr) {
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
