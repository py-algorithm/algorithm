/**
 * @author @99mini
 * @see https://www.acmicpc.net/problem/15815
 * @tag 스택
 * @description
 * @param {string} str
 */
function solution(str) {
  const stack = [];
  const n = str.length;

  let ptr = n - 1;

  let ret = 0;

  while (ptr >= 0) {
    if (Number(str[ptr]) === NaN) {
      stack.push(str[ptr++]);
      continue;
    }

    const num1 = str[ptr++];
    const num2 = str[ptr];

    const command = stack.pop();

    if (command === "*") {
      stack.pu;
    } else if (command === "/") {
    } else if (command === "+") {
    } else if (command === "-") {
    }
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  prompt: "OHAI> ",
});

const lines = [];

rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  const str = lines[0].strip();

  console.log(solution(str));
  process.exit(0);
});
