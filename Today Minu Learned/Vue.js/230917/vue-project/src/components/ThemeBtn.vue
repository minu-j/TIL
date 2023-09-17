<script setup lang="ts">
import { onMounted, ref } from 'vue'

const isDarkMode = ref<boolean>(false)

const getTheme = () => localStorage.getItem('user-theme')
const getMediaPreference = () =>
  window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'

onMounted(() => {
  const prevSetMode = getTheme() === 'dark' || getMediaPreference() === 'dark'
  console.log(prevSetMode)
  isDarkMode.value = prevSetMode ? true : false
  document.documentElement.className = prevSetMode ? 'dark-mode' : ''
})

const toggleTheme = () => setTheme(!isDarkMode.value)

const setTheme = (isDark: boolean) => {
  localStorage.setItem('user-theme', isDark ? 'dark' : 'light')
  isDarkMode.value = isDark
  document.documentElement.className = isDark ? 'dark-mode' : ''
}
</script>

<template>
  <div>
    <button @click="toggleTheme">{{ isDarkMode }}</button>
  </div>
</template>

<style scoped></style>
