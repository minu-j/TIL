<template>
  <div>
    <input
      v-model="todoTitle"
      @keyup.enter="createTodo"
      type="text"
    >
  </div>
</template>

<script>
export default {
    name: 'TodoForm',
    data: function () {
      return {
        todoTitle: null,
      }
    },
    methods: {
      createTodo: function () {
        this.$emit('create-todo', this.todoTitle)
        this.todoTitle = null
      }
    }
}
</script>

<style>

</style>