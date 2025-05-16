/**
 * @author @99mini
 * @see https://www.acmicpc.net/problem/13901
 * @tag 구현, 시뮬레이션
 * @description
 */
function solution(r, c, k, b, s, d) {
  const field = Array.from({ length: r }, () =>
    Array.from({ length: c }).fill(0)
  );

  b.forEach(([row, col]) => {
    field[row][col] = -1;
  });

  // 1: 위
  // 2: 아래
  // 3: 좌
  // 4: 우
  const dn = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];

  let [currRow, currCol] = s;
  field[currRow][currCol] = -1;
  let cnt = 0;
  let nextDirection = 0;

  while (cnt < 4) {
    const dir = d[nextDirection];

    const nr = dn[dir - 1][0] + currRow;
    const nc = dn[dir - 1][1] + currCol;

    if (0 > nr || nr >= r || 0 > nc || nc >= c || field[nr][nc] === -1) {
      cnt++;
      nextDirection = (nextDirection + 1) % 4;
      continue;
    }

    field[nr][nc] = -1;

    currRow = nr;
    currCol = nc;
    cnt = 0;
  }

  return `${currRow} ${currCol}`;
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
  lines.push(line.trim().split(" "));
}).on("close", () => {
  const [r, c] = lines[0].map(Number);
  const k = Number(lines[1]);
  const b = lines.slice(2, k + 2).map((v) => v.map(Number));
  const s = lines[k + 2].map(Number);
  const d = lines[k + 3].map(Number);

  console.log(solution(r, c, k, b, s, d));
  process.exit(0);
});
