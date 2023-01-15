import React from 'react';
import styled from 'styled-components';
import { useDispatch } from 'react-redux';
import { ADD_TODO } from '../stores/types';

function AddButton() {
  const dispatch = useDispatch()

  return (
    // 추가 버튼 클릭시 새로운 todo 생성
    <AddBtn onClick={() => dispatch({type: ADD_TODO})}>
      <Plus>+</Plus>
    </AddBtn>
  );
}

export default AddButton;

const AddBtn = styled.div`
  cursor: pointer;
  position: fixed;
  bottom: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 80px;
  height: 80px;
  background-color: #9747FF;
  border-radius: 80px;
`

const Plus = styled.div`
  font-size: 60px;
  color: white;
  font-weight: 800;
  line-height: 0px;
  margin-bottom: 5px;
`