// 1번
const nums = [1,2,3,4,5,6,7,8]

// for (const i = 0; i < nums.length; i++) {
//   console.log()
// }

// for (const i = 0; i < nums.length; i++) {
//                                     ^

// TypeError: Assignment to constant variable.

// 답

for (let i = 0; i < nums.length; i++) {
  console.log(i)
}

// 0
// 1
// 2
// 3
// 4
// 5
// 6
// 7

// 풀이 : const로 변수를 선언하면 변수의 재선언이 불가하여 반복문을 돌면서 해당 값을 바꿀수가 없으므로 let으로 변수를 선언해준다.

// 2번
// for (num in nums) {
//   console.log(num, typeof num)
// }

// 0 string
// 1 string
// 2 string
// 3 string
// 4 string
// 5 string
// 6 string
// 7 string

// 답

for (const num of nums) {
  console.log(num, typeof num)
}

// 1 number
// 2 number
// 3 number
// 4 number
// 5 number
// 6 number
// 7 number
// 8 number

// 풀이 : in문은 반복문을 돌리면 string으로 출력되므로 of문을 쓴다.