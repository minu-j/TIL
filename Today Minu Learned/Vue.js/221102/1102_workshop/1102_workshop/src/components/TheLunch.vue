<template>
  <div>
    <h1>점심 메뉴</h1>
    <button @click="pickMenu">Pick One</button>
  </div>
</template>

<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
<script>
  import _ from 'lodash'
  
  export default {
    name: 'TheLunch',
    data: function () {
      return {
        lunchMenu: ['짜장면', '짬뽕', '짬짜면'],
      }
    },
    methods: {
      pickMenu: function () {
        const menu = _.sample(this.lunchMenu)
        this.$emit('pick-menu', menu)
      }
    }
  }
</script>

<style>

</style>