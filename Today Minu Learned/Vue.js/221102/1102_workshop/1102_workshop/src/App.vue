<template>
  <div id="app">
    <the-lunch
      @pick-menu="pickMenu"/>
    <p>{{ menu }}</p>
    <hr>
    <the-lotto v-if="this.menu" :menu="menu" @get-numbers="getNumbers"/>
    <p v-if="this.numbers">{{ numbers.sort((a, b) => a - b) }}</p>
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
  data: function () {
    return {
      menu: '',
      numbers: null,
    }
  },
  methods: {
    pickMenu: function (menu) {
      this.menu = menu
    },
    getNumbers: function (menu) {
      this.numbers = [0, 0, 0, 0, 0, 0]
      for (let i = 0; i < this.numbers.length; i++) {
        while (true) {
          const num = _.random(1, 46)
          if (num !== this.numbers[i]) {
            this.numbers[i] = num
            break
          }
        }

      }
      console.log(this.numbers)
    }
  }
}
</script>

<style>

</style>
