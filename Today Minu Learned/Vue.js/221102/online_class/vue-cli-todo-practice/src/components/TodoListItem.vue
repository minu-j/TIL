<template>
  <li>
    <p>{{ todo.title }}</p>
    <button @click="deleteTodo">삭제</button>
  </li>
</template>

<script>
export default {
    name: 'TodoListItem',
    props: {
        todo: Object,
    },
    methods: {
      deleteTodo: function () {
        this.$emit('delete-todo', this.todo)
      }
    }
}
</script>

<style>

</style>