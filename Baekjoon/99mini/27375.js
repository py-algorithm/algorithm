/**
 * @author: 99mini
 * @see https://www.acmicpc.net/problem/27375
 * @tag 브루트포스 알고리즘, 백트래킹
 * @description
 * 1. 5일 동안의 수업 스케줄을 입력받는다. (단, 금요일은 필터링)
 * 2. 각 수업의 시작 시간과 종료 시간을 기준으로 스케줄을 정렬한다.
 * 3. 스케줄을 정렬한 후, 각 수업의 시작 시간과 종료 시간을 기준으로 스케줄을 그룹화한다.
 * 4. 백트래킹을 통해 가능한 조합을 탐색한다.
 * 5. 각 조합의 점수를 계산하고, k와 일치하는 경우 카운트한다.
 */
function solution(lines) {
  const k = Number(lines[0][1]);
  const schedule = lines
    .slice(1)
    .filter((line) => Number(line[0]) !== 5)
    .map((v) => v.map(Number))
    .sort((a, b) => {
      if (a[0] === b[0]) {
        return a[1] - b[1];
      }
      return a[0] - b[0];
    })
    .reduce((acc, curr) => {
      const [day, startTime, endTime] = curr;
      if (!acc[day]) {
        acc[day] = [[startTime, endTime]];
      } else {
        acc[day].push([startTime, endTime]);
      }
      return acc;
    }, {});

  let answer = 0;

  function backtrack(day, endTime, grade) {
    if (grade > k) {
      return;
    }

    if (grade === k) {
      answer++;
      return;
    }

    for (let i = day; i < 5; i++) {
      if (!schedule[i]) {
        continue;
      }
      for (const [currStartTime, currEndTime] of schedule[i]) {
        if ((day === i && endTime < currStartTime) || day < i) {
          grade += currEndTime - currStartTime + 1;
          backtrack(i, currEndTime, grade);
          grade -= currEndTime - currStartTime + 1;
        }
      }
    }
  }

  backtrack(1, 0, 0);

  console.log(answer);
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
  solution(lines);
  process.exit(0);
});
