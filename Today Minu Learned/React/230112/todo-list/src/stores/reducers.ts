import { addTodo, checkTodo, saveTodo, deleteCountTodo, deleteTodo } from './actions'
import { ADD_TODO, CHECK_TODO, SAVE_TODO, DELETE_COUNT_TODO, DELETE_TODO } from './types'

// todo 타입 선언
export type todo = {
  id: number
  content: string
  isCompleted: boolean
  created: string
  deleteCnt: number
}

// state 타입 선언
export type State = {
  todos: todo[]
  pk: number
}

// 초기 state값 지정
const initialState: State = { todos: [], pk: 0 }

// 액션의 타입 지정
type Action =
  | ReturnType<typeof addTodo>
  | ReturnType<typeof checkTodo>
  | ReturnType<typeof saveTodo>
  | ReturnType<typeof deleteCountTodo>
  | ReturnType<typeof deleteTodo>

const reducer = (state: State = initialState, action: Action) => {
  const newState = { ...state }
  const nowDate = new Date()

  switch (action.type) {
    // Todo list 추가
    case ADD_TODO:
      newState.todos.unshift({
        id: newState.pk,
        content: '',
        isCompleted: false,
        created: `${nowDate.getFullYear()}-${String(nowDate.getMonth() + 1).padStart(2, '0')}-${String(nowDate.getDate()).padStart(2, '0')} ${String(nowDate.getHours()).padStart(2, '0')}:${String(nowDate.getMinutes()).padStart(2, '0')}`,
        deleteCnt: 0
      })
      newState.pk++
      break

    // 완료 체크 또는 체크 해제
    case CHECK_TODO:
      newState.todos.filter((todo: todo) => {
        if (todo.id === action.todo.id) {
          todo.isCompleted = !todo.isCompleted
        }
        return true
      })
      newState.todos.sort((a: todo, b: todo) => {
        // 완료, 미완료 순 정렬
        if (a.isCompleted > b.isCompleted) return 1;
        if (a.isCompleted < b.isCompleted) return -1;

        // id 내림차순 정렬
        if (b.id < a.id) return -1;
        if (b.id > a.id) return 1;

        // 모두 같을 경우 정렬하지 않음
        return 0;
      })
      break

    // Todo 저장
    case SAVE_TODO:
      newState.todos.filter((todo: todo) => {
        if (action.payload.id === todo.id) {
          todo.content = action.payload.content
        }
        return true
      })
      break

    case DELETE_COUNT_TODO:
      newState.todos.filter((todo: todo) => {
        if (action.payload.id === todo.id) {
          todo.deleteCnt++
        }
        return true
      })
      break

    // todo 삭제
    case DELETE_TODO:
      // 삭제하려는 id를 가진 todo를 필터링
      const filterdTodo = newState.todos.filter((todo: todo) => 
        todo.id === action.payload.id ? false : true
      )
      newState.todos = [...filterdTodo]
  }
  return newState
}

export default reducer

export type StateType = ReturnType<typeof reducer>