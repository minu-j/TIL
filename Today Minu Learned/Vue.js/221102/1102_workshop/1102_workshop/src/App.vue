<template>
  <div id="app">
    <the-lunch
      @pick-menu="pickMenu"/>
    <hr>
    <the-lotto/>
  </div>
</template>

<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
<script>
import TheLotto from './components/TheLotto.vue'
import TheLunch from './components/TheLunch.vue'

export default {
  name: 'App',
  components: {
    TheLunch,
    TheLotto
  },
  methods: {
    pickMenu: function (menu) {
      console.log(menu)
    }
  }
}
</script>

<style>

</style>
