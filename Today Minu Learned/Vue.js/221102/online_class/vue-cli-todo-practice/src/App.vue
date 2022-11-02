<template>
  <div id="app">
    <TodoForm @create-todo="createTodo"/>
    <TodoList
      :todos="todos"
      @delete-todo="deleteTodo"
    />
    
  </div>
</template>

<script>
import TodoForm from './components/TodoForm.vue'
import TodoList from './components/TodoList.vue'

export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList,
  },
  data: function () {
    return {
      todos: []
    }
  },
  methods: {
    createTodo: function (todoTitle) {
      const todo = {
        title: todoTitle
      }
      this.todos.push(todo)
    },
    deleteTodo: function (todo) {
      const index = this.todos.indexOf(todo.title)
      this.todos.splice(index, 1)
    },
  }
}
</script>

<style>

</style>
