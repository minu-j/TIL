import React, { ChangeEvent, EventHandler, useState } from 'react';
import styled from 'styled-components';
import { useDispatch } from 'react-redux';

import { todo } from '../stores/reducers'
import { CHECK_TODO, UNCHECK_TODO, SAVE_TODO } from '../stores/types'

interface todoData extends todo {
  focusedTodo: number | null
  setFocusedTodo: (value: number | null) => void
  isCompleted: boolean
}

function TodoComponent(props: todoData) {

  const dispatch = useDispatch()

  return (
    <Container>
      <TodoData>
        <TodoCreated content={props.content} isCompleted={props.isCompleted}>{props.created}</TodoCreated>
        {props.focusedTodo === props.id
          ? <TodoInput 
              placeholder="새로운 TODO"
              value={props.content}
              onChange={(e: any) => dispatch({type: SAVE_TODO, payload: {id: props.id, content: e.target.value}})}
              onKeyUp={(e: KeyboardEvent & ChangeEvent<HTMLInputElement>) => {
                if (e.key === 'Enter') {
                  dispatch({type: SAVE_TODO, payload: {id: props.id, content: e.target.value}})
                  props.setFocusedTodo(null)
                }
              }}
              autoFocus></TodoInput>
          : props.content === '' 
            ? <TodoContent 
                onClick={() => {
                  if (!props.isCompleted) {
                    props.setFocusedTodo(props.id)
                  }
                }}
                content={props.content} 
                isCompleted={props.isCompleted}
              >새로운 TODO</TodoContent>
            : <TodoContent 
                onClick={() => {
                  if (!props.isCompleted) {
                    props.setFocusedTodo(props.id)
                  }                
                }}
                content={props.content} 
                isCompleted={props.isCompleted}
              >{props.content}</TodoContent>
        }
      </TodoData>
      <Checkbox onClick={() => {
        if (props.isCompleted) {
          dispatch({type: UNCHECK_TODO, todo: props})
        } else {
          dispatch({type: CHECK_TODO, todo: props})
        }
      }}>
        {props.isCompleted ? <CheckboxMark></CheckboxMark> : null}
      </Checkbox>
    </Container>
  );
}

export default TodoComponent;

interface todoProps {
  content: string | null
  isCompleted: boolean
}

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

const TodoCreated = styled.div<todoProps>`
  font-weight: 400;
  font-size: 16px;
  ${props => {
    if (props.isCompleted) {
      return 'color: #D9D9D9;'
    } else {
      return 'color: black;'
    }
  }}
`

const TodoInput = styled.input<any>`
  padding: 0px;
  margin-top: 5px;
  font-weight: 700;
  font-size: 24px;
  font-family: 'Noto Sans KR', sans-serif;
  border: none;
  &::placeholder {
    color: #D9D9D9;
  }
`

const TodoContent = styled.div<todoProps>`
  width: 100%;
  margin-top: 10px;
  font-weight: 700;
  font-size: 24px;
  word-break: break-all;
  ${props => {
    if (props.isCompleted) {
      return 'color: #D9D9D9; text-decoration-line: line-through;'
    } else if(props.content === '') {
      return 'color: #D9D9D9;'
    } else {
      return 'color: black;'
    }
  }}
  margin-bottom: 5px;
`

const Checkbox = styled.div`
  cursor: pointer;
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