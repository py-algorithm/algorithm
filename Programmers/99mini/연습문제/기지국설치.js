/**
 * @link https://school.programmers.co.kr/learn/courses/30/lessons/12979
 * 카테고리
 *   - BFS
 *   - DFS
 * 문제풀이
 * 알파벳 후 순 정렬. DFS 탐색
 */
function solution(n, stations, w) {
  var answer = 0;

  const arr = Array.from({ length: n }).fill(0);

  stations.forEach((s) => {
    for (let i = Math.max(s - w - 1, 0); i < Math.min(s + w, n); i++) {
      arr[i] = 1;
    }
  });

  for (let i = 0; i < n - w; i += w) {
    if (!arr[i]) {
      console.log(i);
      answer++;
      for (let j = Math.max(i - w, 0); j < Math.min(i + w + 1, n); j++) {
        arr[j] = 1;
      }
    }
  }

  return answer;
}

const testCase = [
  [[11, [4, 11], 1], 3],
  [[16, [9], 2], 3],
];

for (const [test, expected] of testCase) {
  const [n, stations, w] = test;
  const result = solution(n, stations, w);

  console.log(`result:`, result);
  console.log("expected:", expected);

  console.log(result === expected ? "Success" : "Fail");
}
