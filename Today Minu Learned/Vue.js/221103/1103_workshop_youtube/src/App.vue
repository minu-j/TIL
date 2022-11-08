<template>
  <div class="background" id="app">
    <div class="main-box">
      <div>
        <div @click="theme">
          <img v-if="!dark" class="click-able logo" alt="Vue logo" src="./assets/logo.png">
          <img v-if="dark" class="click-able logo" alt="Vue logo" src="./assets/logo-dark.png">
        </div>
        <h1 class="click-able" @click="home">VueTube</h1>
      </div>
      <div class="serch-box-large">
        <the-serch-bar :dark="dark" @search-keyword="getSearch"/>
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
    <img class="video-image" :src="videoImage" alt="">
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
    VideoList,
  },
  data: function () {
    return {
      dark: false,
      search: '',
      searchUrl: 'https://www.googleapis.com/youtube/v3/search',
      key: '',
      part: 'snippet',
      type: 'video',
      items: [],
      videoId: '',
      videoImage: '',
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
    playVideo: function (id, high) {
      this.videoId = id
      this.videoImage = high
    },
    home: function () {
      this.search = ''
      this.videoId = ''
    },
    theme: function () {
      if (this.dark) {
        document.body.classList.remove('dark')
        document.body.classList.add('light')
      }
      else {
        document.body.classList.add('dark')
        document.body.classList.remove('light')

      }
      this.dark = !this.dark
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
  padding-top: 60px;
}
.light {
  color: #2c3e50;
}
.dark {
  background-color: #292929;
  color: whitesmoke;
}
.logo {
  width: 100px;
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
body {
  margin: 0px;
}
.video-image {
  position:absolute;
  width: 100%;
  left: 0px;
  top: 0px;
  z-index: -1;
  opacity: 20%;

}
</style>
