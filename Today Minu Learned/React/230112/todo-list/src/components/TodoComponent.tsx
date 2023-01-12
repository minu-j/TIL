import React from 'react';
import styled from 'styled-components';

import { todo } from '../stores/reducers'

function TodoComponent(props: any) {
  return (
    <Container>
      <TodoData>
        <CreateTime>2023-01-11 09:00</CreateTime>
        <TodoContent>{props.notCompleted}</TodoContent>
      </TodoData>
      <Checkbox>
        <CheckboxMark></CheckboxMark>
      </Checkbox>
    </Container>
  );
}

export default TodoComponent;

const Container = styled.div`
  display: flex;
  align-items: center;
  width: 90%;
  min-height: 100px;
  border-radius: 20px;
  box-shadow: 0px 4px 16px rgba(0, 0, 0, 0.25);
  margin-bottom: 25px;
`

const TodoData = styled.div`
  display: flex;
  flex-direction: column;
  width: 70%;
  padding: 20px;
`

const CreateTime = styled.div`
  font-weight: 400;
  font-size: 16px;
`

const TodoContent = styled.div`
  width: 100%;
  margin-top: 5px;
  font-weight: 700;
  font-size: 24px;
  word-break: break-all;
`

const Checkbox = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background: #D9D9D9;
  border-radius: 8px;
`

const CheckboxMark = styled.div`
  width: 24px;
  height: 24px;
  background: #9747FF;
  box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.25);
  border-radius: 4px;
`