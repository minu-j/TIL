function solution(my_string) {
    var answer = [];
    for (i of my_string) {
        answer.push(i)
    }
    return answer.reverse().join('');
}

console.log(solution("jaron"))