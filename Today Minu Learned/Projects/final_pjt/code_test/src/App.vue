<template>
  <div id="app">
    <star-rating/>
    <get-location @user-location="userLocation"/>
    <kakao-map @search-result-theater="searchResultTheater" :user-location-data="userLocationData"/>
    <movie-time-table :search-result-theater-data="searchResultTheaterData"/>
    <movie-recommend/>
  </div>
</template>

<script>
import StarRating from './components/StarRating.vue'
import MovieRecommend from './components/MovieRecommend.vue'
import GetLocation from './components/GetLocation.vue'
import KakaoMap from './components/KakaoMap.vue'
import MovieTimeTable from './components/MovieTimeTable.vue'

export default {
  name: 'App',
  components: {
    StarRating,
    MovieRecommend,
    GetLocation,
    MovieTimeTable,
    KakaoMap,
  },
  data() {
    return {
      userLocationData: null,
      searchResultTheaterData: {},
    }
  },
  methods: {
    userLocation(userLocation) {
      this.userLocationData = userLocation
    },
    searchResultTheater(searchResultTheater) {
      this.searchResultTheaterData = searchResultTheater
    }
  }
}
</script>

<style>

</style>
