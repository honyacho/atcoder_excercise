const fs = require("fs");
const line = fs.readFileSync("/dev/stdin");
const N = Number(line);
let res = 0;

for (let i = 1; i <= N; i++) {
  const n = Math.floor(N / i);
  res += (i * n * (n + 1)) / 2;
}

console.log(res);
