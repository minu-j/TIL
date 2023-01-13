import { addTodo, checkTodo, uncheckTodo, saveTodo } from './actions'
import { ADD_TODO, CHECK_TODO, UNCHECK_TODO, SAVE_TODO } from './types'

export type todo = {
  id: number
  content: string
  created: string
}

export type State = {
  todos: todo[]
  completeTodos: todo[]
}

const initialState: State = { todos: [], completeTodos: [] }

type Action =
  | ReturnType<typeof addTodo>
  | ReturnType<typeof checkTodo>
  | ReturnType<typeof uncheckTodo>
  | ReturnType<typeof saveTodo>

const reducer = (state: State = initialState, action: Action) => {
  const newState = { ...state }
  const nowDate = new Date()

  switch (action.type) {
    case ADD_TODO:
      newState.todos.unshift({
        id: newState.todos.length,
        content: '',
        created: `${nowDate.getFullYear()}-${String(nowDate.getMonth() + 1).padStart(2, '0')}-${String(nowDate.getDate()).padStart(2, '0')} ${String(nowDate.getHours()).padStart(2, '0')}:${String(nowDate.getMinutes()).padStart(2, '0')}`
      })
      break
    case CHECK_TODO:
      console.log(action.todo, action.completeTodo)
      let i = 0
      newState.todos.filter((todo: todo) => {
        if (action.todo.id === todo.id) {
          console.log(todo)
          newState.completeTodos.push(...newState.todos.splice(i, 1))
        }
        i++
      })
      console.log(newState)
      break
    case UNCHECK_TODO:
      console.log(action.todo, action.completeTodo)
      let j = 0
      newState.completeTodos.filter((todo: todo) => {
        if (action.todo.id === todo.id) {
          console.log(todo)
          newState.todos.push(...newState.completeTodos.splice(j, 1))
        }
        j++
      })
      console.log(newState)
      break
    case SAVE_TODO:
      newState.todos.filter((todo: todo) => {
        if (action.payload.id === todo.id) {
          todo.content = action.payload.content
        }
      })
  }
  return newState
}

export default reducer

export type StateType = ReturnType<typeof reducer>