<template>
  <div>
  </div>
</template>

<script>

export default {
  name: 'GetLocation',
  data() {
    return {
      userLocation: { // 사용자 위치정보
        latitude: null,
        longitude: null,
      },
    }
  },
  methods: {
    getUserLocation() { // 사용자 위치정보 요청 함수
      navigator.geolocation.getCurrentPosition((position) => {
        this.userLocation.latitude = position.coords.latitude
        this.userLocation.longitude = position.coords.longitude
      })
      this.$emit('user-location', this.userLocation)
    },
  },
  mounted() {
    // 접속시 사용자 위치정보 요청
    this.getUserLocation()
  }
}
</script>

<style>

</style>