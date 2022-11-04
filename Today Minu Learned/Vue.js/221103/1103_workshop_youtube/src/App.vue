<template>
  <div id="app">
    <div class="main-box">
      <div>
        <img class="click-able" @click="home" alt="Vue logo" src="./assets/logo.png">
        <h1 class="click-able" @click="home">VueTube</h1>
      </div>
      <div class="serch-box-large">
        <the-serch-bar @search-keyword="getSearch"/>
      </div>
    </div>
    <div>
      <div>
        <div class="video-detail" v-if="videoId">
          <video-detail :video-id="videoId"/>
        </div>
        <div class="search-box" v-if="search">
          <p>{{ search }}에 대한 검색 결과</p>
          <video-list @video-id="playVideo" :items="items"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
import TheSerchBar from './components/TheSerchBar.vue'
import VideoDetail from './components/VideoDetail.vue'
import VideoList from './components/VideoList.vue'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    TheSerchBar,
    VideoDetail,
    VideoList
  },
  data: function () {
    return {
      search: '',
      searchUrl: 'https://www.googleapis.com/youtube/v3/search',
      key: '',
      part: 'snippet',
      type: 'video',
      items: [],
      videoId: '',
    }
  },
  methods: {
    getSearch: function (keyword) {
      this.search = keyword
      axios.get(this.searchUrl + `?key=${this.key}` + `&part=${this.part}` + `&type=${this.type}` + `&q=${keyword}`)
       .then(response => {
          this.items = response.data.items
        })
    },
    playVideo: function (id) {
      this.videoId = id
    },
    home: function () {
      this.search = ''
      this.videoId = ''
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.click-able:hover {
  cursor: pointer;
}
.main-box {
  justify-content:center
}
.serch-box-large {
  display: flex;
  justify-content:center;
  margin: 20px;
}
.video-detail {
  margin-bottom: 30px;
}
</style>
