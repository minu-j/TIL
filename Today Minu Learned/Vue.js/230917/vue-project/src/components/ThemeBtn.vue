<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue'

const isDark = ref<boolean>(false)
const isSystemDark: MediaQueryList = window.matchMedia('(prefers-color-scheme: dark)')
const handleSystemDarkChange = (e: MediaQueryListEvent) => {
  localStorage.removeItem('theme-mode')
  e.matches ? setTheme(true) : setTheme(false)
}

onMounted(() => {
  const userTheme = localStorage.getItem('theme-mode')
  if (userTheme) {
    isDark.value = userTheme === 'dark' ? true : false
    document.documentElement.className = userTheme === 'dark' ? 'dark-mode' : ''
  } else {
    isDark.value = isSystemDark ? true : false
    document.documentElement.className = isSystemDark ? 'dark-mode' : ''
  }
  isSystemDark.addEventListener('change', handleSystemDarkChange)
})

onUnmounted(() => {
  isSystemDark.removeEventListener('change', handleSystemDarkChange)
})

const toggleTheme = () => {
  isDark.value ? setTheme(false) : setTheme(true)
  localStorage.setItem('theme-mode', isDark.value ? 'dark' : 'light')
}

const setTheme = (mode: boolean) => {
  isDark.value = mode
  document.documentElement.className = mode ? 'dark-mode' : ''
}
</script>

<template>
  <div>
    <button @click="toggleTheme">{{ isDark }}</button>
  </div>
</template>

<style scoped></style>
