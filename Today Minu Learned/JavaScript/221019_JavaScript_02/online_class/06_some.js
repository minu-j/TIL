const arr = [1, 2, 3, 4, 5]

// const result = arr.some(function (elem) {
//   return elem % 2 === 0
// })

const result = arr.some((elem) => elem % 2 === 0)

console.log(result)