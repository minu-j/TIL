<template>
  <div>
    <div class="serch-box">
      <input @keyup.enter="search" v-model="searchKeyword" type="text">
      <button @click="search">검색</button>
    </div>
  </div>
</template>

<script>
export default {
 name: 'TheSerchBar',
 data () {
  return {
    searchKeyword: '',
  }
 },
 props: {
  dark: Boolean,
 },
 methods: {
  search: function () {
    this.$emit('search-keyword', this.searchKeyword)
    this.searchKeyword = null
  }
 }
}
</script>

<style>
.serch-box {
  display: flex;
  border:solid #48d98b 1px;
  background: white;
}
button {
  width: 60px;
  height: 30px;
  border: none;
  background: #48d98b;
  color: #2c3e50;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-weight: bold;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
button:hover {
  cursor: pointer;
}
input {
  width: 200px;
  height: 24px;
  border: none;
  outline: none;
  padding-left: 5px;
}
</style>