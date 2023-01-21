import React, { useState } from 'react';
import styled from 'styled-components';
import { useSelector } from 'react-redux';

import Header from './components/Header'
import AddButton from './components/AddButton'
import TodoComponent from './components/TodoComponent'
import { StateType, todo } from './stores/reducers';

import Btn from './Btn';
import LikeBtn from './LikeBtn';

const JURASSIC_GREEN_50 = '#DCFAE3';
const JURASSIC_GREEN_100 = '#BCEDC6';
const JURASSIC_GREEN_200 = '#95DBA3';
const JURASSIC_GREEN_300 = '#6BCB80';
const JURASSIC_GREEN_400 = '#4CC068';
const JURASSIC_GREEN_500 = '#21B44F';
const JURASSIC_GREEN_600 = '#14A647';
const JURASSIC_GREEN_700 = '#00913A';
const JURASSIC_GREEN_800 = '#00812F';
const JURASSIC_GREEN_900 = '#00631E';
const MANGO_YELLOW_50 = '#FBF8E7';
const MANGO_YELLOW_100 = '#F8EDB9';
const MANGO_YELLOW_200 = '#F4E289';
const MANGO_YELLOW_300 = '#F2D856';
const MANGO_YELLOW_400 = '#F1CE31';
const MANGO_YELLOW_500 = '#F2C619';
const MANGO_YELLOW_600 = '#F2C619';
const MANGO_YELLOW_700 = '#F1A604';
const MANGO_YELLOW_800 = '#F39800';
const MANGO_YELLOW_900 = '#F37700';
const BASALT_GRAY_50 = '#FCFCFC';
const BASALT_GRAY_100 = '#E6E5E9';
const BASALT_GRAY_200 = '#CFCED7';
const BASALT_GRAY_300 = '#B9B7C4';
const BASALT_GRAY_400 = '#A2A0B1';
const BASALT_GRAY_500 = '#8C899F';
const BASALT_GRAY_600 = '#75728C';
const BASALT_GRAY_700 = '#615F75';
const BASALT_GRAY_800 = '#4E4C5F';
const BASALT_GRAY_900 = '#3A3948';
const DARK_INFORMATIVE = '#68C7EF';
const DARK_DANGER = '#FB4656';
const LIGHT_INFORMATIVE = '#1790C3';
const LIGHT_DANGER = '#F33041';

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
      <Btn label={"로그인"} color={"green"} type={0} disabled={ false }></Btn>
      <Btn label={"로그인"} color={"green"} type={1} disabled={ false }></Btn>
      <Btn label={"로그인"} color={"green"} type={2} disabled={ false }></Btn>
      <Btn label={"로그인"} color={"green"} type={0} disabled={ true }></Btn>
      <Btn label={"로그인"} color={"green"} type={1} disabled={ true }></Btn>
      <Btn label={"로그인"} color={"green"} type={2} disabled={ true }></Btn>
      <LikeBtn></LikeBtn>
      {/* <Btn label={"로그인"} color={"green"} type={1} disabled={false}></Btn>
      <Btn label={"로그인"} color={"green"} type={2} disabled={false}></Btn> */}
      {/* <Header></Header>
      <AddButton></AddButton>
      {todos} */}
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