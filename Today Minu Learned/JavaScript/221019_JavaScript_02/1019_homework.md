# 221019 homework

## 1. 아래의 설명을 읽고 T/F 여부를 작성하시오

- `False` : let, const은 var과 다르게 동일한 키워드로 다시 변수 선언을 하지 못한다는 차이점이 있다.

- `False` : null은 typeof 출력시 object가 반환된다.

    ```javascript
    > const a = null

    > const b = undefined

    > typeof a
    'object'

    > typeof b
    'undefined'
    ```

- `False` : 배열의 요소를 순회하며 꺼내는 반복문은 of 문이며, in 문은 object의 key를 순회할 때 사용한다.

- `False` : 값과 타입이 같은지 비교하는 이항연산자는 '===' 이다. '==' 연산자는 타입이 다르더라도 true 가 반환된다.

## 2. 아래 같이 numbers 배열이 주어졌을 때, 아래 요구사항들에 맞도록 코드를 작성하시오

```javascript
const numbers = [1, 2, 3, 4, 5]
```

- for … of 문을 사용하여 배열의 각 요소를 출력하시오.

```javascript
for (const number of numbers) {
    console.log(number)
}
```

- for … of 문을 사용하여 배열의 각 요소에 10을 더한 요소들로 구성된 새로운 배열을 생
성하시오.

```javascript
const new_numbers = []

for (const number of numbers) {
  new_numbers.push(number + 10)
}

console.log(new_numbers)
```

- for … of 문을 사용하여 배열의 각 요소들 중 홀수 요소 들로만 구성된 새로운 배열을 생
성하시오.

```javascript
const new_numbers = []

for (const number of numbers) {
  if (number % 2 === 1) {
    new_numbers.push(number)
  }
}

console.log(new_numbers)
```

- for … of 문을 사용하여 배열의 각 요소들을 모두 더한 값을 구하시오.

```javascript
let new_numbers = 0

for (const number of numbers) {
  new_numbers += number
}

console.log(new_numbers)
```
