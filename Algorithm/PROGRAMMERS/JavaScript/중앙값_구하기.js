function solution(array) {
    let center = parseInt(array.length / 2);
    array.sort((a, b) => a - b)
    let answer = array[center];
    return answer;
}


console.log(solution([1, 2, 7, 10, 11]))