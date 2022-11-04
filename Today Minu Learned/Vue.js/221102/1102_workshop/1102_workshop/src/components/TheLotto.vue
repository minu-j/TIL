<template>
  <div>
    <h1>{{ menu }} 먹고 로또</h1>
    <button @click="getNumbers">Get Lucky Numbers</button>
  </div>
</template>

<script>

  export default {
    name: 'TheLotto',
    props: {
      menu: String,
    },
    data: function () {
      return {
        numbers: [0, 0, 0, 0, 0, 0],
      }
    },
    methods: {
      getNumbers: function () {
        this.$emit('get-numbers')
      }
    }
  }
</script>

<style>

</style>