const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  prompt: "OHAI> ",
});

const lines = [];

rl.on("line", (line) => {
  /** 입력 받는 영역 */
  lines.push(line.split(" "));
}).on("close", () => {
  /** 문제 해결 영역 */

  /** 문제 해결 예시 */
  let answer = 0;

  console.log(answer);
  process.exit(0);
});
