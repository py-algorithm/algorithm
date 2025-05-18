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
function solution(n, m, graph, start, end) {
  const queue = () => {
    let head = null;
    let tail = null;
    let length = 0;

    return {
      get length() {
        return length;
      },
      pop: () => {
        const ret = head.value;
        head = head.next;
        length--;
        return ret;
      },
      push: (value) => {
        const newItem = { value, next: null };
        if (head === null) {
          head = newItem;
        } else {
          tail.next = newItem;
        }
        tail = newItem;
        length++;
      },
    };
  };

  /**
   * @type Record<number, Record<number, number>>
   */
  const g = {};

  graph.forEach(([s, e, w]) => {
    if (s in g) {
      if (e in g[s]) {
        g[s][e] = Math.min(g[s][e], w);
      } else {
        g[s][e] = w;
      }
    } else {
      g[s] = {};
      g[s][e] = w;
    }
  });

  const targetEdge = g[start];

  /**
   * @type number[]
   */
  const dist = Array.from({ length: n }).fill(Number.MAX_SAFE_INTEGER);

  dist[start - 1] = 0;

  function bfs(s) {
    const q = queue();
    q.push(s);

    while (q.length) {
      const currentNode = q.pop();

      const nextNodes = Object.entries(g[currentNode]);

      for (const [node, weight] of nextNodes) {
        const nextWeight = dist[node - 1] + g[node];

        if (nextWeight > dist[node - 1]) {
          continue;
        }

        q.push(node);
        dist[node - 1] = nextWeight;
      }
    }
  }

  bfs(start);

  return dist[end - 1];
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
  const n = Number(lines[0]);
  const m = Number(lines[1]);
  const graph = lines.slice(2, 2 + m).map((v) => v.map(Number));
  const [start, end] = lines[lines.length - 1].map(Number);

  console.log(solution(n, m, graph, start, end));
  process.exit(0);
});
