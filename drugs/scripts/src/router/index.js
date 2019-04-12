import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '../components/HomePage.vue'
import Test from '../components/Test.vue'
import Drug from '../components/Drug.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: '/Test',
      name: 'Test',
      component: Test
    },
    {
      path: '/items/:id',
      name: 'Drug',
      component: Drug
    },
  ]
})
