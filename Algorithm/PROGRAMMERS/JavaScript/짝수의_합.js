function solution(n) {
    let answer = 0;
    let i = 1
    while (i <= n) {
        if (i % 2 === 0) {
            answer += i
        } i++
    }
    return answer
}
