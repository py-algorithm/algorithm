/**
 * @author @99mini
 * @see https://www.acmicpc.net/problem/1913
 * @tag 구현
 * @description
 */
function solution(n, target) {
  const grid = Array.from({ length: n }).map((_) =>
    Array.from({ length: n }).fill(0)
  );

  let depth = 1;

  const center = Math.floor(n / 2);

  /** 문제 해결 예시 */
  let answer = `${center + 1} ${center + 1}`;

  let row = center;
  let col = center;

  let count = 1;

  grid[row][col] = count;

  /**
   * [row, col] 방향
   * 반시계 방향으로 회전
   */
  let directionList = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
  ];

  let direction = 0;

  const validateDirection = (row, col) => {
    const rowDiff = row - center;
    const colDiff = col - center;

    if (row === center - 1 && col === center) {
      direction++;
      return;
    }

    if (rowDiff === depth && colDiff === depth) {
      // 우측 상단
      direction++;
    } else if (rowDiff === -1 * depth && colDiff === depth) {
      // 우측 하단
      direction++;
    } else if (rowDiff === depth && colDiff === -1 * depth) {
      // 좌측 하단
      direction++;
    } else if (rowDiff === -1 * (depth + 1) && colDiff === -1 * depth) {
      // 좌측 상단
      depth++;
      direction++;
    }

    direction %= 4;
  };

  while (count < n * n) {
    const [dr, dc] = directionList[direction];

    row += dr;
    col += dc;

    grid[row][col] = ++count;

    validateDirection(row, col);

    if (count === target) {
      answer = `${row + 1} ${col + 1}`;
    }
  }

  for (const itemRow of grid) {
    console.log(itemRow.join(" "));
  }

  console.log(answer);
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

  const n = Number(lines[0]);
  const target = Number(lines[1]);

  solution(n, target);

  process.exit(0);
});
