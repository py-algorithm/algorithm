/**
 * @link https://school.programmers.co.kr/learn/courses/30/lessons/12979
 * 카테고리
 *   - 그리디
 * 문제풀이
 * 시작점과 끝점을 갱신하며 그리드 알고리즘 구현
 */
function solution(n, stations, w) {
  var answer = 0;
  const range = 2 * w + 1;
  let start = 1;
  let end = 0;

  for (const s of stations) {
    end = s - w - start;

    if (s - w > start) {
      answer += Math.ceil(end / range);
    }

    start = s + w + 1;
  }

  if (start <= n) {
    end = n + 1 - start;
    answer += Math.ceil(end / range);
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
