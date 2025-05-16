/**
 * @author: @99mini
 * @see https://www.acmicpc.net/problem/11779
 * @tag
 * - 그래프 이론
 * - 최단 경로
 * - 데이크스트라
 * - 역추적
 * @description
 * @param {number} n
 * @param {number} m
 * @param {[number, number, number][]} graph
 * @param {number} start
 * @param {number} end
 */
function solution(n, m, graph, start, end) {}

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
  const m = Number(lines[1]);
  const graph = lines.slice(2, 2 + m).map((v) => v.map(Number));
  const [start, end] = lines[lines.length - 1].map(Number);

  console.log(solution(n, m, graph, start, end));
  process.exit(0);
});
