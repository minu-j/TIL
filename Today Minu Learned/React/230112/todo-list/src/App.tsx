import React, { useState } from 'react';
import styled from 'styled-components';
import { useSelector } from 'react-redux';

import Header from './components/Header'
import AddButton from './components/AddButton'
import TodoComponent from './components/TodoComponent'
import { StateType, todo } from './stores/reducers';

function App() {
  const [focusedTodo, setFocusedTodo] = useState<number | null>(null)

  const todos = useSelector((state: StateType) => {
    const TodoComponentList: JSX.Element[] = []
    state.todos.map((todo: todo) => 
      TodoComponentList.push(<TodoComponent
        key={todo.id}
        focusedTodo={focusedTodo}
        setFocusedTodo={setFocusedTodo}
        id={todo.id}
        content={todo.content}
        isCompleted={todo.isCompleted}
        created={todo.created}
        deleteCnt={todo.deleteCnt}
      ></TodoComponent>)
    )
    return TodoComponentList
  })

  return (
    <AppContainer>
      <Header></Header>
      <AddButton></AddButton>
      {todos}
    </AppContainer>
  );
}

export default App;

const AppContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100vw;
  min-height: 100vh;
  max-width: 390px;
  background-color: white;
`
