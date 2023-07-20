function solution(numbers) {
  if (!Math.max(...numbers)) {
    return "0";
  }
  const ans = numbers
    .sort((a, b) => Number(`${b}${a}`) - Number(`${a}${b}`))
    .join("");
  return ans;
}
