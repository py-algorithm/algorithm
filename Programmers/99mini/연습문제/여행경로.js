/**
 * @link https://school.programmers.co.kr/learn/courses/30/lessons/43164
 * 카테고리
 *   - BFS
 *   - DFS
 * 문제풀이
 * 알파벳 후 순 정렬. DFS 탐색
 */
function solution(tickets) {
  const answer = [];

  const graph = {};
  const visited = ["ICN"];

  for (const [s, e] of tickets) {
    if (s in graph) {
      graph[s].push(e);
    } else {
      graph[s] = [e];
    }
  }

  Object.entries(graph).forEach(([key, value]) => {
    graph[key] = value.sort((a, b) => b.localeCompare(a));
  });

  while (visited.length) {
    const now = visited[visited.length - 1];

    if (!(now in graph) || graph[now].length === 0) {
      answer.push(visited.pop());
    } else {
      visited.push(graph[now].pop());
    }
  }

  return answer.reverse();
}

const testCase = [
  [
    [
      ["ICN", "JFK"],
      ["HND", "IAD"],
      ["JFK", "HND"],
    ],
    ["ICN", "JFK", "HND", "IAD"],
  ],
  [
    [
      ["ICN", "SFO"],
      ["ICN", "ATL"],
      ["SFO", "ATL"],
      ["ATL", "ICN"],
      ["ATL", "SFO"],
    ],
    ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"],
  ],
];

for (const [test, expected] of testCase) {
  const result = solution(test);

  console.log(`result:`, result);
  console.log("expected:", expected);

  let success = true;
  for (let i = 0; i < expected.length; i++) {
    if (result[i] !== expected[i]) {
      success = false;
      break;
    }
  }

  console.log(success ? "Success" : "Fail");
}
