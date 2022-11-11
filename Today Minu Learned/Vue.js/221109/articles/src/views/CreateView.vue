<template>
  <div>
    <h1>글 작성</h1>
    <form @submit.prevent="createArticle">
      <input v-model.trim="title" type="text"><br>
      <textarea v-model="content" name="" id="" cols="30" rows="10"></textarea>
      <input type="submit" value="제출">
    </form>
    <router-link :to="{ name: 'index' }">뒤로가기</router-link>
  </div>
</template>

<script>
export default {
  name: 'CreateView',
  data() {
    return {
      title: null,
      content: null,
    }
  },
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content
      const payload = {
        title, content
      }
      this.$store.dispatch('createArticle', payload)
      this.$router.push({ name: 'index' })
    }
  }
}
</script>

<style>

</style>