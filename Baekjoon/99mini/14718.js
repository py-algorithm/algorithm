/**
 * @author @99mini
 * @see https://www.acmicpc.net/problem/14718
 * @tag
 * - 브루트포스 알고리즘
 * @description
 * @param {number} n - enemy
 * @param {number} k - goal
 * @param {[number, number, number][]} stats
 */
function solution(n, k, stats) {
  const [powerStat, dexStat] = stats.reduce(
    (acc, [power, dex, _]) => {
      acc[0].push(power);
      acc[1].push(dex);

      return acc;
    },
    [[], []]
  );

  const sortedStat = stats.sort((a, b) => a[2] - b[2]);

  let answer = Number.MAX_SAFE_INTEGER;

  for (const p of powerStat) {
    for (const d of dexStat) {
      let intStat = 0;
      let cnt = 0;
      for (let i = 0; i < n; i++) {
        if (sortedStat[i][0] <= p && sortedStat[i][1] <= d) {
          cnt++;
          intStat = sortedStat[i][2];
          if (cnt === k) {
            answer = Math.min(answer, p + d + intStat);
            break;
          }
        }
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
  const [n, k] = lines[0].map(Number);
  const stats = lines.slice(1).map((v) => v.map(Number));

  console.log(solution(n, k, stats));
  process.exit(0);
});
