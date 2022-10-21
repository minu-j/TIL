function solution(str1, str2) {
    var answer = 2;
    const len = str2.length
    for (i in str1) {
        for (j in str2) {
            if (str1[i] === str2[j]) {
                slice_str = str1.slice(i, (Number(i) + str2.length))
                if (str2 === slice_str) {
                    answer = 1
                    break
                }
            }
        }
        if (answer === 1) {
            break
        }
    }
    return answer;
}

console.log(solution("ppprrrogrammers", "pppp"))