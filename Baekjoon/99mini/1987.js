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
    const [r, c] = input[0].split(" ");
    const grid = input.slice(1);

    let visited = Array.from({ length: "Z".charCodeAt() - "A".charCodeAt() + 1 }).fill(false);

    const dn = [
      [1, 0],
      [-1, 0],
      [0, 1],
      [0, -1],
    ];

    function isBoundary(row, col) {
      return 0 <= row && row < r && 0 <= col && col < c;
    }

    function solution() {
      let ret = 0;

      function dfs(row, col, depth) {
        ret = Math.max(ret, depth);

        visited[grid[row][col].charCodeAt() - "A".charCodeAt()] = true;

        for (const [dr, dc] of dn) {
          const [nextRow, nextCol] = [row + dr, col + dc];

          if (!isBoundary(nextRow, nextCol)) {
            continue;
          }

          const currentAlphaIndex = grid[nextRow][nextCol].charCodeAt() - "A".charCodeAt();

          if (!visited[currentAlphaIndex]) {
            dfs(nextRow, nextCol, depth + 1);
            visited[currentAlphaIndex] = false;
          }
        }
      }

      dfs(0, 0, 1);

      return ret;
    }

    console.log(solution());
    process.exit();
  });
