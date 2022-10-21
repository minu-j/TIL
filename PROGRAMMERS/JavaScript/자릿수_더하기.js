function solution(n) {
    const num = String(n);
    var answer = 0;

    for (i of num) {
        answer += Number(i)
    }

    return answer;
}

console.log(solution(9876))