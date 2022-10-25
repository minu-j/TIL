function solution(numbers) {
    numbers = numbers.sort((a, b) => b - a)
    var answer = numbers[0] * numbers[1];
    return answer;
}

console.log(solution([0, 31, 24, 10, 1, 9]))