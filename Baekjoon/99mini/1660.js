const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
readline
  .on("line", function (line) {
    input = line.split(" ").map((el) => parseInt(el));
  })
  .on("close", function () {
    const n = parseInt(input[0]);
    const balls = [];

    let b = 0;
    let i = 1;

    while (b < n) {
      b += Math.floor((i * (i + 1)) / 2); // 정사면체에 필요한 포탄의 개수. 1, 4, 10, 20
      balls.push(b);
      i += 1;
    }

    let dp = Array.from({ length: n + 1 }).fill(Number.MAX_SAFE_INTEGER);

    for (let i = 1; i < n + 1; i++) {
      for (const b of balls) {
        if (b === i) {
          dp[i] = 1;
        }
        if (b >= i) {
          break;
        }
        dp[i] = Math.min(dp[i], 1 + dp[i - b]);
      }
    }

    console.log(dp[n]);
    process.exit();
  });
