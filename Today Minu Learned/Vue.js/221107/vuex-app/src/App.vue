<template>
  <div id="app">
    <h1>{{ message }}</h1>
    <input v-model="inputData" @keyup.enter="changeMessage" type="text">
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {
  },
  data() {
    return {
      inputData: null,
    }
  },
  computed: {
    message() {
      return this.$store.state.message
    }
  },
  methods: {
    changeMessage() {
      const newMessage = this.inputData
      this.$store.dispatch('changeMessage', newMessage)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
