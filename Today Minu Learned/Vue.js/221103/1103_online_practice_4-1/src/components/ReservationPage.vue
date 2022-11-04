<template>
  <div>
    <h2>예약 페이지</h2>
    <div class="bb-3">
      <div>
        <button @click="selectTime(item)"
          class="button-size button-not"
          :class="{ 'button-selected': item[1] }"
          v-for="(item, index) in times"
          :key="`time-${index}`"
        > 
          {{ item[0] }}
        </button>
      </div>
      <div v-if="selectedTimes.length">
        <hr>
        <div>
          <span>선택 시간: </span>
          <span v-for="(select, index) in selectedTimes" :key="`selected-${index}`">
            {{ select }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ReservationTime',
  data: function () {
    return {
      times: [],
      selectedTimes: [],
      reservatedTimes: '',
    }
  },
  methods: {
    selectTime: function (t) {
      if (this.selectedTimes.includes(t[0])) {
        const p = this.selectedTimes.indexOf(t)
        this.selectedTimes.splice(p)
        this.times[this.times.indexOf(t)][1] = !this.times[this.times.indexOf(t)][1]
      } else {
        if (this.selectedTimes.length < 5) {
          this.selectedTimes.push(t[0])
          this.times[this.times.indexOf(t)][1] = !this.times[this.times.indexOf(t)][1]
        } else {
        alert("5타임까지만 신청할 수 있습니다.")
      }
      }
      console.log(this.selectedTimes)
    }
  },
  mounted: function () {
      for (let t = 0; t < 48; t++) {
        const H = parseInt(t / 2)
        let M = 0
        if (t % 2 === 0) {
          M = '00'
        } else {
          M = '30'
        }
        const time = [H + ':' + M, false]
        this.times.push(time)
      }
  }
}
</script>

<style>
hr {
  width: 50%;
  border: 0px;
  height: 2px;
  background: #2c3e50;
  margin-top: 20px;
  margin-bottom: 20px;
}
.bb-3 {
  padding-bottom: 30px;
}
span {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 700;
  margin: 5px;
}
button {
  font-family: 'Noto Sans KR', sans-serif;
  width: 60px;
  height: 25px;
  margin: 4px;
}
button:hover {
  background: #658dc63d;
  cursor: pointer;
}
.button-not {
  border: none;
  background: none;
  color: #84898c;
}
.button-selected {
  border: none;
  background: #658dc63d;
  color: #0f4c81;
}
</style>