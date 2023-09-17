<script setup lang="ts">
import { onMounted } from 'vue'
import { googleOneTap } from 'vue3-google-login'
import type { CallbackTypes } from 'vue3-google-login'

const callback: CallbackTypes.CodeResponseCallback = (response) => {
  console.log('Authorisation code', response.code)
}

onMounted(() => {
  googleOneTap()
    .then((response) => {
      // This promise is resolved when user selects an account from the the One Tap prompt
      console.log('Handle the response', response)
    })
    .catch((error) => {
      console.log('Handle the error', error)
    })
})
</script>

<template><GoogleLogin :callback="callback" /></template>

<style scoped lang="scss"></style>
