function solution(n) {
    let i = 1
    while (true) {
        if ((i * 6) % n  === 0) {
            break
        } i++
    }

    return i;
}

console.log(solution(4))