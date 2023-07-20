const fs = require("fs");
const [[n, m], days] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((value) => value.split(" ").map((value) => Number(value)));
let ans = days.slice(0, m).reduce((a, b) => a + b, 0);
let income = ans;
for (let i = m; i < n; i++) {
  income = income - days[i - m] + days[i];
  ans < income ? (ans = income) : null;
}
console.log(ans);
