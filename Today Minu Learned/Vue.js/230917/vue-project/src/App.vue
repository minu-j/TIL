<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import ThemeBtn from './components/ThemeBtn.vue'
</script>

<template>
  <header>
    <ThemeBtn></ThemeBtn>
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
      <RouterLink to="/barcode">Barcode</RouterLink>
      <RouterLink to="/login">Login</RouterLink>
    </nav>
  </header>

  <RouterView />
</template>
