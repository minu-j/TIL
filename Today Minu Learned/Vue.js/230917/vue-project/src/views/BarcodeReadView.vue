<script setup lang="ts">
import { StreamBarcodeReader } from 'vue-barcode-reader'
import { onMounted, ref } from 'vue'
import MobileDetect from 'mobile-detect'

const code = ref('스캔중')
const isMobile = ref('')

const onDecode = (value: string) => {
  code.value = value
}
const onLoaded = () => {
  console.log('Ready to start scanning barcodes')
}
onMounted(() => {
  const md = new MobileDetect(window.navigator.userAgent)
  isMobile.value = md.mobile() ?? 'null'
})
</script>

<template>
  <div>{{ isMobile }}</div>
  <div class="barcode-scanner-container">
    <StreamBarcodeReader @decode="onDecode" @loaded="onLoaded" />
  </div>

  <div>{{ code }}</div>
</template>

<style lang="scss">
.barcode-scanner-container {
  width: 400px;
}
.scanner-container {
  & {
    .laser {
      display: none;
    }
    .overlay-element {
      display: none;
    }
  }
}
</style>
