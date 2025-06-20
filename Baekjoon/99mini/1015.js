/**
 * @author @99mini
 * @see https://www.acmicpc.net/problem/1015
 * @tag 정렬
 * @description
 * @param {number} n
 * @param {number[]} arr
 */
function solution(n, arr) {
  const N = arr.length;
  const arrObjList = arr.map((value, idx) => ({ value, idx }));
  arrObjList.sort((a, b) => a.value - b.value || a.idx - b.idx);

  const P = Array(N);

  for (let i = 0; i < N; i++) {
    P[arrObjList[i].idx] = i;
  }
  return P.join(" ");
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
  const n = Number(lines[0]);
  const arr = lines[1].map(Number);

  console.log(solution(n, arr));
  process.exit(0);
});
