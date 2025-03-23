/**
 * @author 99mini
 * @link https://www.acmicpc.net/problem/17241
 * 카테고리
 *   - 그래프 이론
 *   - 그래프 탐색
 * 문제 풀이
 * !`console.log()`를 여러 번 호출 시 시간초과가 발생!
 * 결과값을 모아두었다가 한 번에 출력해한다.
 * @see https://mule-heo.tistory.com/242
 */
function solution(visited, graph, target) {
  const result = [];
  for (const t of target) {
    let ret = 0;
    const current = graph[t];

    if (visited[t] === -2) {
      result.push(ret);
      continue;
    }

    if (visited[t] === 0) {
      visited[t] = -2;
      ret++;
    }

    for (const c of current) {
      if (visited[c] === 0) {
        visited[c] = -1;
        ret++;
      }
    }

    result.push(ret);
  }

  return result;
}

const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];

readline
  .on("line", function (line) {
    input.push(line);
  })
  .on("close", function () {
    const [n, m, q] = input[0].split(" ").map(Number);
    const graph = {};

    for (let i = 1; i < n + 1; i++) {
      graph[i] = [];
    }

    for (let i = 1; i < m + 1; i++) {
      const [a, b] = input[i].split(" ").map(Number);
      graph[a].push(b);
      graph[b].push(a);
    }

    const target = [];

    for (let i = m + 1; i < m + 1 + q; i++) {
      target.push(parseInt(input[i]));
    }

    const visited = Array.from({ length: n + 1 }).fill(0);

    const ret = solution(visited, graph, target);
    console.log(ret.join("\n"));
    process.exit(0);
  });
