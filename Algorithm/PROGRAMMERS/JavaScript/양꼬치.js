function solution(n, k) {
    service = parseInt(n / 10)
    const answer = n * 12000 + (k - service) * 2000
    return answer
}