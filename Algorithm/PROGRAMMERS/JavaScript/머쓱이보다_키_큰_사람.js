function solution(array, height) {
    var answer = 0;
    for (let i of array.sort().reverse()) {
        if (i > height) {
            answer++
        } else {
            break
        }
    }
    return answer;
}

console.log(solution([149, 180, 192, 170], 167))