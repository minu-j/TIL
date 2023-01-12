# Redux

자바스크립트 앱을 위한 예측 가능한 상태 컨테이너

1. 애플리케이션이 모든 상태는 하나의 스토어 안에 하나의 객체 트리 구조로 저장된다.

2. 상태를 변화시키는 유일한 방법은 무슨 일이 벌어지는지 묘사하는 액션 객체를 전달하는 방법 뿐이다.

3. 액션에 의해 상태 트리가 어떻게 변화하는지 지정하기 위해 순수 리듀서를 작성해야 한다.

## 리덕스를 설정하는 방법

### 1. store를 생성한다.

```js
import { createStore } from 'redux'

const store = createStore(reducer)
```

### 2. reducer를 정의한다.

```js
import { Provider, useSelector, useDispatch, connect } from 'react-redux'

function reducer(currentState, action) {
  if (currentState === undefined) { // 설정된 state가 없을 경우
    return {
      // state의 초기값
    }
  }
  // 기존 state 복사
  const newState = { ...currentState }

  // 새로운 state를 
  return newState
}
```

* `provider`: state를 어떤 컴포넌트에 제공할 것인가 정의

```html
<Provider store={ store }>
  <!--  -->
</Provider>
```

* `useSelector()`: state의 값을 구독

```js
const number = useSelector(state => state.number)
```

* `useDispatch()`: state의 값을 변경

```js
dispatch({ type: 'TYPE' })

// ...

if (action.type === 'TYPE') {
  newState.number++
}
```


## 리덕스가 작동하는 방법

### 1. action을 통해 변경되는 값을 전달한다.

* action은 type과 변경될 값을 가진다.

### 2. dispatch 함수로 action을 reducer로 전달한다.

### 3. reducer는 새로운 state를 생성한다.

* type이 일치하는 동작 실행

* 기존 state를 기반으로 새로운 state 생성