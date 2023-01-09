# React 주요 개념

## React 가장 단순한 예시

```js
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<h1>Hello, world!</h1>);

// Hello, world!
```

---

## JSX

JavaScript + HTML의 확장 문법

### React.createElement()

Babel은 JSX를 React.createElement() 호출로 컴파일함.

```js
const element = (
  <h1 className="greeting">
    Hello, world!
  </h1>
);

const element = React.createElement(
  'h1',
  {className: 'greeting'},
  'Hello, world!'
);
```

---

## 엘리먼트

엘리먼트는 React 앱의 가장 작은 단위이며, 화면에 표시할 내용을 기술함.

React 앱은 하나의 root DOM 노드를 가지며, React 엘리먼트를 렌더링하기 위해서는 DOM 엘리먼트를 ReactDom.createRoot()에 전달한 다음, React 엘리먼트를 root.render()에 전달해야 함.

> ### 렌더링 된 엘리먼트 업데이트하기
>
> React 엘리먼트를 업데이트하기 위해서는 새로운 엘리먼트를 생성하고 이를 root.render()로 전달해야 함.
>
> 전체 엘리먼트를 재생성하더라도 React Dom은 해당 엘리먼트와 자식 엘리먼트를 이전의 엘리먼트와 비교하여 DOM을 원하는 상태로 만드는데 필요한 경우에만 DOM을 업데이트 함.

---

## Components와 Props

### 함수형 컴포넌트

```js
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

### 클래스 컴포넌트

```js
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```

### 사용자 정의 컴포넌트

```js
const element = <Welcome name="Sara" />;
```

### Props
```js
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

const root = ReactDOM.createRoot(document.getElementById('root'));
const element = <Welcome name="Sara" />;
root.render(element);
```

---

## State와 Lifecycle

### State 올바르게 사용하기

1. 직접 state를 수정하지 않고 setState()를 통해 수정

2. State 업데이트는 비동기적일 수 있으므로 기존 state 값에 의존해서는 안됨.
    ```js
    // Wrong
    this.setState({
      counter: this.state.counter + this.props.increment,
    });

    // Correct
    this.setState((state, props) => ({
      counter: state.counter + props.increment
    }));

    // Correct
    this.setState(function(state, props) {
      return {
        counter: state.counter + props.increment
      };
    });
    ```

3. State 업데이트는 병합되며, 별도의 setState() 호출로 변수를 독립적으로 업데이트할 수 있음.

### 데이터는 아래로 흐른다.

컴포넌트는 자신의 state를 자식 컴포넌트에 props로 전달할 수 있음.

모든 state는 특정한 컴포넌트가 소유하고 있으며, 그 state로부터 파생된 UI 또는 데이터는 오직 자신의 아래에 있는 컴포넌트에만 영향을 미침.

---

## Event

* React의 이벤트는 소문자 대신 카멜케이스를 사용

* JSX를 사용하여 문자열이 아닌 함수로 이벤트 핸들러를 전달

```html
<!-- HTML -->
<button onclick="activateLasers()">
  Activate Lasers
</button>
```

```js
// React
<button onClick={activateLasers}>
  Activate Lasers
</button>
```

* 반드시 preventDefault를 명시적으로 호출해야 함.

```js
// 예시
function Form() {
  function handleSubmit(e) {
    e.preventDefault();
    console.log('You clicked submit.');
  }

  return (
    <form onSubmit={handleSubmit}>
      <button type="submit">Submit</button>
    </form>
  );
}
```

### 이벤트 핸들러에 인자 전달

```js
<button onClick={(e) => this.deleteRow(id, e)}>Delete Row</button>
<button onClick={this.deleteRow.bind(this, id)}>Delete Row</button>
```

---

## 조건부 렌더링

### if로 return 분기

```js
function Greeting(props) {
  const isLoggedIn = props.isLoggedIn;
  if (isLoggedIn) {
    return <UserGreeting />;
  }
  return <GuestGreeting />;
}

const root = ReactDOM.createRoot(document.getElementById('root')); 
// Try changing to isLoggedIn={true}:
root.render(<Greeting isLoggedIn={false} />);
```

### 논리 && 연산자로 if를 인라인 표현

`true && expression = expression`

`false && expression = false`

```js
return (
    <div>
      <h1>Hello!</h1>
      {unreadMessages.length > 0 &&
        <h2>
          You have {unreadMessages.length} unread messages.
        </h2>
      }
    </div>
  );

```

### 조건부 연산자로 if-else 인라인 표현

`condition ? true: false`

```js
return (
    <div>
      The user is <b>{isLoggedIn ? 'currently' : 'not'}</b> logged in.
    </div>
  );
```

### 컴포넌트가 렌더링하는 것을 막기

```js
return null
```

---

## 리스트와 key

리스트의 반복의 경우 key 에러 경고를 표시함.

엘리먼트에 안정적인 고유성을 부여하기 위해 배열 내부의 엘리먼트에 key를 지정

```js
const todoItems = todos.map((todo) =>
  <li key={todo.id}>
    {todo.text}
  </li>
);
```

* 추출된 컴포넌트의 경우 추출된 컴포넌트 내부 태그가 아닌, 정의된 컴포넌트 태그에 key값을 정의해야 함.

```js
function ListItem(props) {
  // 맞습니다! 여기에는 key를 지정할 필요가 없습니다.
  return <li>{props.value}</li>;
}

function NumberList(props) {
  const numbers = props.numbers;
  const listItems = numbers.map((number) =>
    // 맞습니다! 배열 안에 key를 지정해야 합니다.
    <ListItem key={number.toString()} value={number} />
  );
  return (
    <ul>
      {listItems}
    </ul>
  );
}
```

* key는 배열 안에서 형제 사이에서만 고유해야 하며, 전체 범위에서 고유할 필요는 없음.

* key는 prop과 같은 형식이지만, prop되지는 않음.

---

## Form

