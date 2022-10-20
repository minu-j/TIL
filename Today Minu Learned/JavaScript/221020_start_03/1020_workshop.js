function isPalindrome(str) {
  str_list = []
  let i = 0
  const len_str = str.length
  while (i < len_str) {
    if (str[i] != ' ') {
      str_list.push(str[i])
    }
    i++
  }

  const len_str_list = str_list.length
  let j = 0
  let ans = true
  while (j < len_str_list / 2) {
    if (str_list[j] != str_list[len_str_list - j - 1]) {
      ans = false
      break
    }
    j++
  }
  console.log(ans)
}

// 출력
console.log(
  isPalindrome('a santa at nasa'), // true
  isPalindrome('google') // false
)