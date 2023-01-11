# React Hook

함수형 컴포넌트에서 React state와 Lifecycle을 연동할 수 있게 해주는 함수

## State Hook

`useState`

```js
import React, { useState } from 'react';

function Example() {
  // "count"라는 새 상태 변수를 선언합니다
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}
```

## Effect hook

`useEffect`

```js
import React, { useState, useEffect } from 'react';

function Example() {
  const [count, setCount] = useState(0);

  // componentDidMount, componentDidUpdate와 같은 방식으로
  useEffect(() => {
    // 브라우저 API를 이용하여 문서 타이틀을 업데이트합니다.
    document.title = `You clicked ${count} times`;
  });

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}
```

* React 컴포넌트가 렌더링 이후 어떤 일을 수행해야 하는지 말함.

* useEffect를 컴포넌트 내부에 둠으로써 state 및 props에도 접근할 수 있도록 함.

* 렌더링 이후 매번 수행됨.(effect가 수행되는 시점에서 이미 DOM이 업데이트 되어 있음.)

### Clean-up

함수를 반환하여 컴포넌트가 unmount 또는 re-render될 때 clean-up을 실행함.

```js
// clean-up이 필요할 때
useEffect(() => {
    function handleStatusChange(status) {
      setIsOnline(status.isOnline);
    }

    ChatAPI.subscribeToFriendStatus(props.friend.id, handleStatusChange);
    return () => {
      ChatAPI.unsubscribeFromFriendStatus(props.friend.id, handleStatusChange);
    };
  });

// clean-up이 필요하지 않을 때
  useEffect(() => {
    document.title = `You clicked ${count} times`;
  });
```

### Multiple Effect

각각 다른 일을 하는 effect에 대해 여러개의 effect를 선언할 수 있음.

```js
function FriendStatusWithCounter(props) {
  const [count, setCount] = useState(0);
  useEffect(() => {
    document.title = `You clicked ${count} times`;
  });

  const [isOnline, setIsOnline] = useState(null);
  useEffect(() => {
    function handleStatusChange(status) {
      setIsOnline(status.isOnline);
    }

    ChatAPI.subscribeToFriendStatus(props.friend.id, handleStatusChange);
    return () => {
      ChatAPI.unsubscribeFromFriendStatus(props.friend.id, handleStatusChange);
    };
  });
  // ...
}
```

* useEffect 내의 특정 값이 리렌더링시 변경되지 않는다면, 조건문을 통해 건너뛰는 방법으로 성능 최적화

* clean-up과정을 mount, unmount시 한번씩만 실행하고 싶다면, 두번째 인자로 빈 배열([])을 넘김.

## Hook의 규칙

1. 최상위에서만 Hook을 호출해야 함.

  * effect를 조건부로 실행하기 위해서는 Hook 내부에 조건문을 넣어야 함.

2. React 함수 내에서 Hook을 호출해야 함.

  * 일반적인 JavaScript 함수 내에서 Hook을 호출할 수 없음.