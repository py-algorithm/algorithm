/**
 * @author 99mini
 * @see https://www.acmicpc.net/problem/12851
 * @tag
 * - 그래프 이론
 * - 그래프 탐색
 * - 너비 우선 탐색
 * @description BFS
 * @param {number} n
 * @param {number} k
 */
function solution(n, k) {
  if (n === k) {
    return `${0}\n${1}`;
  }

  const Q = () => {
    let tail = null;
    let head = null;
    let length = 0;

    return {
      get length() {
        return length;
      },
      push: (item) => {
        const newItem = { value: item, next: null };
        if (head === null) {
          head = newItem;
        } else {
          tail.next = newItem;
        }

        tail = newItem;
        length++;
      },
      pop: () => {
        const ret = head.value;
        head = head.next;
        length--;

        return ret;
      },
    };
  };

  let minDepth = Number.MAX_SAFE_INTEGER;
  let combination = 1;

  const q = Q();
  q.push([n, 0]);

  const visited = { [n]: 0 };

  const funcList = [(v) => v + 1, (v) => v - 1, (v) => v * 2];

  while (q.length) {
    const [curr, depth] = q.pop();

    if (depth > minDepth) {
      continue;
    }

    for (const fn of funcList) {
      const nextPos = fn(curr);

      if (0 <= nextPos && nextPos <= 100_000) {
        if (nextPos === k) {
          if (minDepth > depth + 1) {
            minDepth = depth + 1;
          } else if (minDepth === depth + 1) {
            combination++;
          }
        }

        if (visited[nextPos] === undefined || visited[nextPos] === depth + 1) {
          q.push([nextPos, depth + 1]);
          visited[nextPos] = depth + 1;
        }
      }
    }
  }

  return `${minDepth}\n${combination}`;
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

  console.log(solution(n, k));
  process.exit(0);
});
