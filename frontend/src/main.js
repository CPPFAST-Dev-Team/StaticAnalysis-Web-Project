import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import App from './App.vue'
import router from './router'
import axios from 'axios'

axios.defaults.baseURL = import.meta.env.VITE_API_BASE_URL

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

const app = createApp(App)
        .use(router) // Register the router with the app
        .use(pinia)
        .mount('#app')
