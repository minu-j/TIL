function solution(genres, plays) {
  const chart = {};
  for (const genre in genres) {
    if (chart[genres[genre]]) {
      chart[genres[genre]].count++;
      chart[genres[genre]].acc_play += plays[genre];
      chart[genres[genre]].top.push(Number(genre));
      chart[genres[genre]].top.sort((a, b) => plays[b] - plays[a]);
      if (chart[genres[genre]].top.length > 2) {
        chart[genres[genre]].top.pop();
      }
    } else {
      chart[genres[genre]] = {
        count: 1,
        acc_play: plays[genre],
        top: [Number(genre)],
      };
    }
  }

  genre_list = Object.keys(chart).sort(
    (a, b) => chart[b].acc_play - chart[a].acc_play
  );
  const answer = [];
  for (const genre in genre_list) {
    answer.push(...chart[genre_list[genre]].top);
  }

  return answer;
}
