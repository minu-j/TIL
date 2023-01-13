import { ADD_TODO, CHECK_TODO, UNCHECK_TODO, SAVE_TODO } from './types'
import { todo } from "./reducers"

export const addTodo = () => ({ type: ADD_TODO })
export const checkTodo = () => ({ type: CHECK_TODO, todo: <todo>{}, completeTodo: <todo>{} })
export const uncheckTodo = () => ({ type: UNCHECK_TODO, todo: <todo>{}, completeTodo: <todo>{} })
export const saveTodo = () => ({ type: SAVE_TODO, payload: {id: 0, content:''} })