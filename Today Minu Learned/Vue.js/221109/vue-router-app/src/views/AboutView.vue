<template>
  <div class="about">
    <h1>This is an about page</h1>
    <router-link :to="{ name: 'home' }">홈으로</router-link>
    <button @click="toHome">홈으로</button>
    <input @keyup.enter="toHello" v-model="userName" type="text">
  </div>
</template>

<script>
export default {
  name: 'AboutView',
  data() {
    return {
      userName: null
    }
  },
  methods: {
    toHome() {
      this.$router.push({name: 'home'})
    },
    toHello() {
      this.$router.push({name: 'hello', params: { userName: this.userName }})
    }
  }
}
</script>