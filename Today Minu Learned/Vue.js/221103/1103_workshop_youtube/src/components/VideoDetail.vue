<template>
  <div>
    <div>
      <iframe 
        class="play-box"
        width="560" 
        height="315" 
        :src="`https://www.youtube.com/embed/${videoId}?autoplay=1`" 
        title="YouTube video player" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen
      >
      </iframe>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  props: {
    videoId: String,
  }
}
</script>

<style>
.play-box {
  box-shadow: rgba(0, 0, 0, 0.15) 0px 15px 25px, rgba(0, 0, 0, 0.05) 0px 5px 10px;
}
</style>