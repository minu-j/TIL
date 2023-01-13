import React from 'react';
import styled from 'styled-components';
import { useSelector } from 'react-redux';

import { StateType } from '../stores/reducers';

function Header() {
  const notCompleted = useSelector((state: StateType) => state.todos.length)

  return (
    <AppHeader>
      <AppTitle>TODO LIST</AppTitle>
      <TodoCounter>미완료된 TODO 개수
        <UncompletedCount>{notCompleted}개</UncompletedCount>
      </TodoCounter>
    </AppHeader>
  );
}

export default Header;

const AppHeader = styled.div`
  position: -webkit-sticky;
  position: sticky;
  top: 0px;
  width: 100%;
  height: 200px;
  font-family: 'Noto Sans KR', sans-serif;
  background-image: linear-gradient(white 80%, #ffffff00);
`

const AppTitle = styled.h1`
  margin-top: 64px;
  margin-left: 40px;
  font-weight: 800;
  font-size: 40px;
  margin-bottom: 10px;
`

const TodoCounter = styled.span`
  margin-left: 40px;
  font-weight: 400;
  font-size: 16x;
`

const UncompletedCount = styled.span`
  margin-left: 10px;
  font-weight: 700;
  font-size: 24px;
`