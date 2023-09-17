import './styles/main.scss'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import vue3GoogleLogin from 'vue3-google-login'

const app = createApp(App)

app.use(createPinia())
app.use(router)

// https://console.cloud.google.com/projectselector2/apis/
app.use(vue3GoogleLogin, {
  clientId: '503004455609-o22q08itlbdajcsup2n53lbgcrqvampk.apps.googleusercontent.com'
})

app.mount('#app')
