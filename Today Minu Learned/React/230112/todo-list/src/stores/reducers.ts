import { addTodo } from './actions'
import { ADD_TODO } from './types'

export type todo = {
  id?: number
  content?: string | null
  completed?: boolean
  created?: string
}

export type State = {
  todos: todo[]
  notCompleted: number
}

const initialState: State = { todos: [], notCompleted: 0 }

type Action =
  | ReturnType<typeof addTodo>

const reducer = (state: State = initialState, action: Action) => {
  const newState = { ...state }
  switch (action.type) {
    case ADD_TODO:
      newState.todos.push({
        id: newState.todos.length,
        content: null,
        completed: false,
        created: '2023-01-11 09:00'
      })
      newState.notCompleted++
  }
  console.log(newState)
  return newState
}

export default reducer

export type StateType = ReturnType<typeof reducer>