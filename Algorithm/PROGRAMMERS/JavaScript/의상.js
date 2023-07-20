function solution(clothes) {
  const obj = {};
  for (const cloth in clothes) {
    if (obj[clothes[cloth][1]]) {
      obj[clothes[cloth][1]]++;
    } else {
      obj[clothes[cloth][1]] = 2;
    }
  }
  const count = Object.values(obj);
  ans = 1;
  for (const idx in count) {
    ans *= count[idx];
  }
  return ans - 1;
}
