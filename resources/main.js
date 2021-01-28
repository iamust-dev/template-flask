import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import antd from 'ant-design-vue'
import App from './applause/app.vue'
import routes from './applause/routes/all'
import 'ant-design-vue/dist/antd.less'
import './applause/styles/tailwind.css'
import './applause/styles/override.css'

const app = createApp(App)
const router = createRouter({
  history: createWebHistory(),
  routes
})

app.use(antd)
app.use(router)
app.mount('#app')

document.getElementById('app-spin').classList.add('hidden')
