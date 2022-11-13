<template>
  <div>
    <div>
      <p>{{ searchResultTheaterData.place_name }}</p>
      <p>{{ searchResultTheaterData.road_address_name }}</p>
      <p>{{ searchResultTheaterData.phone }}</p>
      <p>{{ searchResultTheaterData.place_url }}</p>
      <p>{{ searchResultTheaterData.distance }}</p>
    </div>
    <div id="time-table" v-for="(movie, index) in timeTable" :key="`movie-${index}`">
      <p>{{ movie.title }} | {{ movie.rating }}</p>
      <div v-for="(theater, index) in movie.theater" :key="`theater-${index}`">
        {{theater.num}}
        <div>
          <a :href="schedule.link" v-for="(schedule, index) in theater.schedule" :key="`schedule-${index}`">
            {{ schedule.time }}
          </a>
        </div>
      </div>
      <hr>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import cheerio from 'cheerio'

export default {
  name: 'MovieTimeTable',
  data() {
    return {
      nearTheater: null,
      timeTable: [],
    }
  },
  props: {
    searchResultTheaterData: Object,
  },
  watch: {
    searchResultTheaterData: function() {
      // const timeTable = document.querySelector('#time-table')
      this.getTimeTable()
    }
  },
  methods: {
    getTimeTable() {
      const url = `/search.naver?query=${this.searchResultTheaterData.place_name}영화시간표`

      axios.get(url)
        .then((response) => {
          this.timeTable = []
          const $ = cheerio.load(response.data)
          $('tbody._wrap_time_table > tr').map((i, element) => {
            const movie = {
              title: null, 
              rating: null,
              theater: []
            }
            movie.rating = $(element).find('th > span').text()
            movie.title = $(element).find('th > a').text()
            $(element).find('td > div').map((i, element) => {
              const theater = {
                num: null,
                schedule: []
              }
              theater.num = $(element).find('span.place').html()

              $(element).find('span.time_info > a').map((i, element) => {
                const schedule = {
                  time: null,
                  link: null
                }
                schedule.time = $(element).text()
                schedule.link = $(element)[0]['attribs']['href']
                theater.schedule.push(schedule)
              })
              movie.theater.push(theater)
            })
            this.timeTable.push(movie)
          })
        })
        .catch((error) => {
          console.log('데이터 수신 실패', error)
        })
    },
  }
}
</script>

<style>

</style>
