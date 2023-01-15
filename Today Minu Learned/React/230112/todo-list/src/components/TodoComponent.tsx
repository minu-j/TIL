import React, { ChangeEvent, useState } from 'react';
import styled, { keyframes } from 'styled-components';
import { useDispatch } from 'react-redux';

import { todo } from '../stores/reducers'
import { CHECK_TODO, DELETE_TODO, DELETE_COUNT_TODO, SAVE_TODO } from '../stores/types'

// todo의 data prop 타입 확장
interface todoData extends todo {
  focusedTodo: number | null
  setFocusedTodo: (value: number | null) => void
}

function TodoComponent(props: todoData) {
  const [deleteTimer, setDeleteTimer] = useState(0)
  // dispatch 선언
  const dispatch = useDispatch()

  return (
    <Container deleteCnt={props.deleteCnt}>
      <TodoData>
        {props.isCompleted === true 
          ? <TodoCreated content={props.content} isCompleted={props.isCompleted}>{4 - props.deleteCnt}초 뒤 삭제...</TodoCreated> 
          : <TodoCreated content={props.content} isCompleted={props.isCompleted}>{props.created}</TodoCreated>
        }
        {props.focusedTodo === props.id
          // 해당 컴포넌트가 포커스될 때 input 표시
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
              isCompleted={props.isCompleted}
              autoFocus></TodoInput>
          // 해당 컴포넌트가 포커스되지 않았을 때는 content 표시
          : props.content === '' 
            // content가 비어있을 때는 임의 문구 표시
            ? <TodoContent 
            onClick={() => {
              if (!props.isCompleted) {
                props.setFocusedTodo(props.id)
              }
            }}
            content={props.content} 
            isCompleted={props.isCompleted}
            >새로운 TODO</TodoContent>
            // content가 비어있지 않을 때는 내용 표시
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
        // 체크박스를 클릭할 때 체크 표시 또는 해제하기
        dispatch({type: CHECK_TODO, todo: props})
        const setDeleteTimer = setInterval(() => {
          dispatch({type: DELETE_COUNT_TODO, payload: { id: props.id }})
        }, 1000)
        
        const deleteTimeout = async () => {
          await setTimeout(() => {
            dispatch({type: DELETE_TODO, payload: { id: props.id }})
            clearInterval(setDeleteTimer)
          }, 4000);
        }
        deleteTimeout()
      }}>
        {props.isCompleted ? <CheckboxMark></CheckboxMark> : null}
      </Checkbox>
    </Container>
  );
}

export default TodoComponent;

interface inputProps {
  onKeyUp: any
  isCompleted: boolean
}

interface todoProps {
  content: string | null
  isCompleted: boolean
}

interface deleteCnt {
  deleteCnt: number
}

const purpleSparkle = keyframes`
  0% {
    background: #9747FF;
  }
  100% {
    background: none;
  }
`

const Container = styled.div<deleteCnt>`
  display: flex;
  align-items: center;
  width: 90%;
  min-height: 100px;
  border-radius: 20px;
  box-shadow: 0px 4px 16px rgba(0, 0, 0, 0.25);
  margin-bottom: 25px;
  background: linear-gradient(to right, #ff4f6a ${props => 100 / 3 * props.deleteCnt}%, white ${props => 100 / 3 * props.deleteCnt}%);
  animation: ${purpleSparkle} 0.3s ease;
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

const TodoInput = styled.input<inputProps>`
  padding: 0px;
  margin-top: 5px;
  font-weight: 700;
  font-size: 24px;
  font-family: 'Noto Sans KR', sans-serif;
  border: none;
  background: none;
  &::placeholder {
    color: #D9D9D9;
  }
  ${props => {
    if (props.isCompleted) {
      return 'color: #D9D9D9; text-decoration-line: line-through;'
    } else {
      return 'color: black;'
    }
  }}
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