<template>
  <div id="app">
    <h1>버튼 박스 제작</h1>
    <div class="reserve-box">
      <div class="box">
        <ReservationPage/>
      </div>
    </div>
  </div>
</template>

<script>
import ReservationPage from './components/ReservationPage.vue'

export default {
  name: 'App',
  components: {
    ReservationPage
  },
  data () {
    return {
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');
#app {
  font-family: 'Noto Sans KR', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.box {
  box-shadow: rgba(255, 255, 255, 0.1) 0px 1px 1px 0px inset, rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;
  width: 600px;

}
.reserve-box {
  display: flex;
  justify-content: center;
}

</style>
