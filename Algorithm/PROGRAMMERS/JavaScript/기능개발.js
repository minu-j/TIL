function solution(progresses, speeds) {
  const answer = [];
  let acc_count = 1;
  let prev_day = 0;
  for (let i = 0; i < progresses.length; i++) {
    const now_day = Math.ceil((100 - progresses[i]) / speeds[i]);
    if (now_day <= prev_day) {
      acc_count++;
    } else if (prev_day && now_day > prev_day) {
      answer.push(acc_count);
      acc_count = 1;
    }
    prev_day = Math.max(prev_day, now_day);
  }
  answer.push(acc_count);
  return answer;
}
