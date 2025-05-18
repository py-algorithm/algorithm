/**
 * @author @99mini
 * @see https://www.acmicpc.net/problem/14716
 * @tag
 * - 그래프 이론
 * - 그래프 탐색
 * - 너비 우선 탐색
 * - 깊이 우선 탐색
 * - 격자 그래프
 * @description
 * @param {number} m - row
 * @param {number} n - col
 * @param {number[][]} grid
 */
function solution(m, n, grid) {
  const dn = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
    [1, -1],
    [-1, 1],
    [1, 1],
    [-1, -1],
  ];

  const visited = Array.from({ length: m }, () =>
    Array.from({ length: n }).fill(0)
  );

  function dfs(row, col) {
    for (const [dr, dc] of dn) {
      const nr = dr + row;
      const nc = dc + col;

      if (0 > nr || nr >= m || 0 > nc || nc >= n) {
        continue;
      }

      if (grid[nr][nc] === 0) {
        continue;
      }

      if (visited[nr][nc] === 1) {
        continue;
      }

      visited[nr][nc] = 1;
      dfs(nr, nc);
    }
  }

  let answer = 0;

  for (let row = 0; row < m; row++) {
    for (let col = 0; col < n; col++) {
      if (grid[row][col] === 1 && visited[row][col] === 0) {
        dfs(row, col);
        answer++;
      }
    }
  }
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
  lines.push(line.split(" "));
}).on("close", () => {
  const [m, n] = lines[0].map(Number);
  const grid = lines.slice(1).map((v) => v.map(Number));

  console.log(solution(m, n, grid));
  process.exit(0);
});
