<template>
  <div>
    <div v-for="(item, index) in items" :key="`video-${index}`">
      <div class="video-list">
        <img :src="item['snippet']['thumbnails']['default']['url']" alt="thumbnails">
        <div class="text-box">
          <p @click="selectVideo(item['id']['videoId'])" class="title">{{ item['snippet']['title'] }}</p>
          <p class="description">{{ item['snippet']['description'] }}</p>
          <p class="channelTitle">{{ item['snippet']['channelTitle'] }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VideoListItem',
  props: {
    items: Array,
  },
  methods: {
    selectVideo: function (id) {
      this.$emit('video-id', id)
    }
  }
}
</script>

<style>
img {
  object-fit: contain
}
.title {
  font-size:large;
  font-weight: bold;
}
.title:hover {
  cursor: pointer;
  color: #48d98b;
}
.channelTitle {
  font-size:medium;
  font-weight: bold;
}
.video-list {
  display: flex;
  text-align: left;
  margin-inline: 40px;
  margin-bottom: 20px;
  box-shadow: rgba(9, 30, 66, 0.25) 0px 4px 8px -2px, rgba(9, 30, 66, 0.08) 0px 0px 0px 1px;
  border-radius: 20px;
  padding-inline: 30px;
}
.text-box {
  padding-inline: 30px;
}
</style>