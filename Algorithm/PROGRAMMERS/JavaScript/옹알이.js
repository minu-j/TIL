function solution(babbling) {
    const words = ["aya", "ye", "woo", "ma"]
    const hardWords = ["ayaaya", "yeye", "woowoo", "mama"]
    const filetrBabbling = []
    count = babbling.length
    let i = 0
    while (i < count) {
        let babbl = babbling.pop()
        for (let hardWord of hardWords) {
            babbl = babbl.replaceAll(hardWord, '*')
        }
        for (let word of words) {
            babbl = babbl.replaceAll(word, '')
        }
        filetrBabbling.push(babbl)
        i++
    }
    var answer = 0;
    for (let j of filetrBabbling) {
        if (j === '') {
            answer++
        }
    }
    return answer;
}

console.log(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))