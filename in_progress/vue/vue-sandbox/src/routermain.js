import './assets/main.css'

import { createRouter, createWebHistory } from 'vue-router'

import HomeView from './components/05_routing/HomeView.vue'
import AboutView from './components/05_routing/AboutView.vue'
import User from './components/05_routing/User.vue'

const routes = [
  { path: '/', component: HomeView },
  { path: '/about', component: AboutView },
  // dynamic segments start with a colon
  { path: '/users/:id', component: User },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

import { createApp } from 'vue'
import RouterApp from './components/05_routing/RouterApp.vue'

createApp(RouterApp)
  .use(router)
  .mount('#app')
