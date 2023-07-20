function solution(s) {
  const stack = [];
  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(") {
      stack.push(1);
    } else {
      const now = stack.pop();
      if (!now) {
        return false;
      }
    }
  }
  if (stack.length) {
    return false;
  }
  return true;
}
