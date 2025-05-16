/**
 * @author @99mini
 * @see https://www.acmicpc.net/problem/14502
 * @tag
 * - 구현
 * - 그래프 이론
 * - 브루트포스 알고리즘
 * - 그래프 탐색
 * - 너비 우선 탐색
 * - 격자 그래프
 * @description BFS + DFS(백트레킹) 조합하여 완전 탐색
 * @param {number} n
 * @param {number} m
 * @param {number[][]} grid
 */
function solution(n, m, grid) {
  let answer = 0;

  const dn = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];

  /**
   * @type [number, number][]
   */
  const virusList = [];
  for (let row = 0; row < n; row++) {
    for (let col = 0; col < m; col++) {
      if (grid[row][col] === 2) {
        virusList.push([row, col]);
      }
    }
  }

  function bfs() {
    const q = virusList.slice();
    let ptr = 0;

    const copiedGrid = grid.map((v) => v.map((_) => _));

    while (q.length > ptr) {
      const [currRow, currCol] = q[ptr++];

      for (const [dr, dc] of dn) {
        const nr = dr + currRow;
        const nc = dc + currCol;

        if (0 > nr || nr >= n || 0 > nc || nc >= m) {
          continue;
        }
        if (copiedGrid[nr][nc] === 0) {
          copiedGrid[nr][nc] = 2;
          q.push([nr, nc]);
        }
      }
    }

    return copiedGrid.flat().filter((v) => v === 0).length;
  }

  /**
   *
   * @param {number} count
   */
  function backtrack(count) {
    if (count === 3) {
      const ret = bfs();
      answer = Math.max(ret, answer);
      return;
    }

    for (let row = 0; row < n; row++) {
      for (let col = 0; col < m; col++) {
        if (grid[row][col] === 0) {
          grid[row][col] = 1;
          backtrack(count + 1);
          grid[row][col] = 0;
        }
      }
    }
  }

  backtrack(0);

  return answer;
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
  const [n, m] = lines[0].map(Number);
  const grid = lines.slice(1).map((v) => v.map(Number));

  console.log(solution(n, m, grid));
  process.exit(0);
});
