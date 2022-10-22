import { createRouter, createWebHistory } from 'vue-router'
import ImageView from '../views/ImageView'
import MapView from '../views/MapView'

const routes = [
  {
    path: '/',
    name: 'image',
    component: ImageView
  },
  {
    path: '/map/',
    name: 'map',
    component: MapView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
