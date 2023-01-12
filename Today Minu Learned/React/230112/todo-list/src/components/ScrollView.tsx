import React from 'react';
import styled from 'styled-components';

function ScrollView() {
  return (
    <AppHeader>

    </AppHeader>
  );
}

export default ScrollView;

const AppHeader = styled.div`
  width: 100%;
  height: 200px;
  font-family: 'Noto Sans KR', sans-serif;
`

const AppTitle = styled.h1`
  margin-top: 64px;
  margin-left: 40px;
  font-weight: 800;
  font-size: 40px;
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