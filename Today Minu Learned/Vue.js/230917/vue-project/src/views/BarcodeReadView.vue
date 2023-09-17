<script setup lang="ts">
import { ref } from 'vue'

const a = ref(0)
</script>

<template>
  <div>{{ a }}</div>
  <button @click="a++">up</button>
</template>

<styles>
</styles>
