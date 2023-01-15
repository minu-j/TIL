import { ADD_TODO, CHECK_TODO, SAVE_TODO, DELETE_COUNT_TODO, DELETE_TODO } from './types'
import { todo } from "./reducers"

export const addTodo = () => ({ type: ADD_TODO })
export const checkTodo = () => ({ type: CHECK_TODO, todo: <todo>{} })
export const saveTodo = () => ({ type: SAVE_TODO, payload: {id: 0, content:''} })
export const deleteCountTodo = () => ({ type: DELETE_COUNT_TODO, payload: {id: 0} })
export const deleteTodo = () => ({ type: DELETE_TODO, payload: {id: 0} })