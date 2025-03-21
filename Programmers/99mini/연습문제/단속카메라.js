/**
 * @link https://school.programmers.co.kr/learn/courses/30/lessons/42884
 * 카테고리
 *   - 그리디
 * 문제풀이
 * 그리디 알고리즘. 관통하는 문제
 * @see https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/?envType=study-plan-v2&envId=leetcode-75
 */
function solution(routes) {
  let answer = 1;
  const n = routes.length;
  const sorted = routes.sort((a, b) => a[1] - b[1]);
  console.log(sorted);

  let pos = sorted[0][1];

  for (let i = 1; i < n; i++) {
    if (routes[i][0] > pos || routes[i][1] < pos) {
      answer += 1;
      pos = routes[i][1];
    }
  }

  return answer;
}

const testCase = [
  [
    [
      [1, 2],
      [3, 4],
      [4, 5],
      [-1, 1],
      [-10, -5],
    ],
    3,
  ],
  [
    [
      [1, 2],
      [3, 4],
      [4, 5],
      [-1, 1],
    ],
    2,
  ],
  [
    [
      [-20, -15],
      [-14, -5],
      [-18, -13],
      [-5, -3],
    ],
    2,
  ],
];

for (const [test, expected] of testCase) {
  const result = solution(test);

  console.log(`result:`, result);
  console.log("expected:", expected);

  console.log(result === expected ? "Success" : "Fail");
}
