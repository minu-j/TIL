function solution(n) {
    var answer = 2;
    if ((Math.sqrt(n)) === parseInt(Math.sqrt(n))) {
        answer = 1
    }
    return answer;
}

console.log(solution(3))