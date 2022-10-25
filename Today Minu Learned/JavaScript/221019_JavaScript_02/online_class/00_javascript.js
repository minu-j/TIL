// 선언식 함수 -> 호이스팅, 함수 호출 이후에 선언해도 동작한다.
//             -> 익명함수 불가능

console.log(add(1, 2))   // 3

function add(num1, num2) {
  return num1 + num2
}

console.log(add(1, 2))   // 3


// 표현식 함수 -> 정의된 함수가 변수로 평가되어 정의 전 호출시 에러 발생
//             -> 익명함수 가능
// console.log(sub(2, 7))   // ReferenceError: Cannot access 'sub' before initialization

const sub = function (num1, num2) {
  return num1 - num2
}

console.log(sub(2, 7))   // -5


// 함수의 기본 인자 선언

const greeting = function (name = 'Anonymous') {
  return `Hi ${name}`
}

console.log(greeting())   // Hi Anonymous


// 화살표 함수 Arrow function => 표현식에서만 사용 가능

const arrow = function (name) {
  return `hello, ${name}`
}

const arrow2 = (name) => { return `hello, ${name}` }

const arrow3 = name => `hello, ${name}`


// 즉시 실행 함수(IIFE, Immediately Invoked Function Expression)

(function (num) { return num ** 3 })(2)

(num => num ** 3)(2)


// Array

const numbers = [1, 2, 3, 4, 5]

console.log(numbers[0])   // 1
console.log(numbers[-1])   // undefined
console.log(numbers.length)   // 5
console.log(numbers[numbers.length - 1])   // 5

// 배열 메서드

numbers.reverse()
console.log(numbers)   // [ 5, 4, 3, 2, 1 ]

numbers.push(100)
console.log(numbers)   // [ 5, 4, 3, 2, 1, 100 ]

numbers.pop()
console.log(numbers)   // [ 5, 4, 3, 2, 1 ]

console.log(numbers.includes(1))   // true
console.log(numbers.includes(100))   // false

console.log(numbers.indexOf(3))   // 2
console.log(numbers.indexOf(100))   // -1

console.log(numbers.join())   // 5,4,3,2,1
console.log(numbers.join(''))   // 54321
console.log(numbers.join(' '))   // 5 4 3 2 1
console.log(numbers.join('-'))   // 5-4-3-2-1
