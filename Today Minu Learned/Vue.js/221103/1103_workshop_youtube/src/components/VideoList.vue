<template>
  <div>
    <video-list-item @video-id="selectVideo" :items="items"/>
  </div>
</template>

<script>
import VideoListItem from './VideoListItem.vue'
export default {
  components: { VideoListItem },
  name: 'VideoList',
  props: {
    items: Array,
  },
  methods: {
    selectVideo: function (id, high) {
      this.$emit('video-id', id, high)
    }
  }
}
</script>

<style>

</style>