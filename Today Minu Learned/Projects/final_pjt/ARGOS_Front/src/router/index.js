import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView'
import TicketView from '@/views/TicketView'
import PlayView from '@/views/PlayView'
import NewsView from '@/views/NewsView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/home',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/ticket',
    name: 'TicketView',
    component: TicketView
  },
  {
    path: '/play',
    name: 'PlayView',
    component: PlayView
  },
  {
    path: '/news',
    name: 'NewsView',
    component: NewsView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
