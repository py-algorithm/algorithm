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

  let left = 0;
  let right = w - 1;

  let leftMax = block[left];
  let rightMax = block[right];

  while (left < right) {
    leftMax = Math.max(leftMax, block[left]);
    rightMax = Math.max(rightMax, block[right]);

    if (leftMax <= rightMax) {
      answer += leftMax - block[left];
      left += 1;
    } else {
      answer += rightMax - block[right];
      right -= 1;
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
