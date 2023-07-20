function solution(priorities, location) {
  let count = 0;
  const visited = new Array(priorities.length);
  let idx = 0;
  let max_priority = Math.max(...priorities);
  while (true) {
    const pointer = idx % priorities.length;
    if (priorities[pointer] === max_priority && !visited[pointer]) {
      visited[pointer] = true;
      priorities[pointer] = -1;
      max_priority = Math.max(...priorities);
      count++;
      if (pointer === location) {
        return count;
      }
    }

    if (count == priorities.length) {
      break;
    }
    idx++;
  }
}
