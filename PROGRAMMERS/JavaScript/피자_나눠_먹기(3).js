function solution(slice, n) {
    let i = 1
    while ((i * slice) < n) {
        i++
    }
    return i;
}

console.log(solution(7, 10))