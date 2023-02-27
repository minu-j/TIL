function solution(denum1, num1, denum2, num2) {
    const denum = denum1 * num2 + denum2 * num1
    const num = num1 * num2
    let i = 2
    let GCN = 1
    while (i < Math.min(denum, num)) {
        if (denum % i === 0 && num % i === 0) {
            GCN = i
        }
        i++
    }
    const answer = [denum / GCN, num / GCN];
    return answer;
}

console.log(solution(9, 2, 1, 3))