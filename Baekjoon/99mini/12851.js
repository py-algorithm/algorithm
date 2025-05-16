/**
 * @author 99mini
 * @see https://www.acmicpc.net/problem/12851
 * @tag
 * - 그래프 이론
 * - 그래프 탐색
 * - 너비 우선 탐색
 * @description BFS
 * @param {number} n
 * @param {number} k
 */
function solution(n, k) {
  let minDepth = Number.MAX_SAFE_INTEGER;
  let combination = 0;

  const q = [[n, 0]];
  let ptr = 0;

  const visited = { [n]: true };

  const funcList = [(v) => v + 1, (v) => v - 1, (v) => v * 2];

  while (q.length > ptr) {
    const [curr, depth] = q[ptr++];

    if (depth > minDepth) {
      continue;
    }

    if (curr === k) {
      if (minDepth === depth) {
        combination++;
      } else if (minDepth > depth) {
        minDepth = depth;
        combination = 1;
      }
      continue;
    }

    for (const fn of funcList) {
      const nextPos = fn(curr);

      if (nextPos in visited) {
        continue;
      }

      q.push([nextPos, depth + 1]);
    }
  }

  return `${minDepth}\n${combination}`;
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
  const [n, k] = lines[0].map(Number);

  console.log(solution(n, k));
  process.exit(0);
});
