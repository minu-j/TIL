function solution(n) {
    const answer = []
    let i = 1
    while (i <= n) {
        if (i % 2 === 1) {
            answer.push(i)
        }
        i++
    }
    return answer;
}

console.log(solution(15))