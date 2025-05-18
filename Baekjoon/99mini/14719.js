/**
 * @author @99mini
 * @see https://www.acmicpc.net/problem/14719
 * @tag
 * - 구현
 * - 시뮬레이션
 * @description
 * @param {number} h - hegiht
 * @param {number} w - width
 * @param {number[]} block
 */
function solution(h, w, block) {
  let answer = 0;
  for (let i = 1; i < w - 1; i++) {
    const left = Math.max(...block.slice(0, i));
    const right = Math.max(...block.slice(i + 1));
    const m = Math.min(left, right);

    if (m > block[i]) {
      answer += m - block[i];
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
  const [h, w] = lines[0].map(Number);
  const block = lines[1].map(Number);

  console.log(solution(h, w, block));
  process.exit(0);
});
