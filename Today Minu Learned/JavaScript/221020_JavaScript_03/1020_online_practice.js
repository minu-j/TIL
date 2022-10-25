console.log('    *    ')
console.log('   ***   ')
console.log('  *****  ')
console.log(' ******* ')
console.log('*********')

let i = 4
star = [' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ']
while (i >= 0) {
  star[i] = star[star.length - i - 1] = '*'
  console.log(star.join(''))
  i--
}
