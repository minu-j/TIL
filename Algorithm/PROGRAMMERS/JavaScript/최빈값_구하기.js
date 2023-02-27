function solution(array) {
    const count_array = []
    for (let i of array) {
        if (count_array[i]) {
            count_array[i] += 1
        } else {
            count_array[i] = 1
        }
    }
    let max_num = 0
    let max_count = 0
    for (let j in count_array) {
        if (count_array[j] > max_count) {
            max_num = parseInt(j)
            max_count = count_array[j]
        }
    }

    count_array.sort((a, b) => b - a)

    let answer = 0
    if (count_array[0] === count_array[1]) {
        answer = -1
    } else {
        answer = max_num
    }
    return answer;
}


console.log(solution([0, 3, 3, 3]))
console.log(solution([1, 1, 2, 2]))
console.log(solution([0]))