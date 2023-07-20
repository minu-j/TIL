function solution(participant, completion) {
  const runners = {};
  let answer = "";
  for (const participant_idx in participant) {
    if (runners[participant[participant_idx]]) {
      runners[participant[participant_idx]]++;
    } else {
      runners[participant[participant_idx]] = 1;
    }
  }
  for (const completion_idx in completion) {
    runners[completion[completion_idx]]--;
  }
  for (const runner in runners) {
    if (runners[runner]) {
      return runner;
    }
  }
}
