const numbers = [90, 80, 70, 100]

// 배열 모든 요소의 총 합

// const sumNum = numbers.reduce(function (result, number) {   // 누적값, 배열
//   return result + number
// }, 0)

// console.log(sumNum)

const sumNum = numbers.reduce((result, number) => result + number, 0)

console.log(sumNum)