// homepage/scripts/index.js
import Vue from 'vue'
import App from './src/App.vue'
import router from './src/router'
import store from './src/store.js';


Vue.config.productionTip = false
import Jumbotron from 'bootstrap-vue/es/components/jumbotron'
Vue.use(Jumbotron)
import Card from 'bootstrap-vue/es/components/card'
Vue.use(Card)
import Layout from 'bootstrap-vue/es/components/layout'
Vue.use(Layout)
import Alert from 'bootstrap-vue/es/components/alert'
Vue.use(Alert)


document.addEventListener("DOMContentLoaded", (context => () => {
  // your JS code here
  let homePageVue = new Vue({
    el: '#app',
    router,
    store,
    components: { App },
    template: '<App />'
  })
  console.log(homePageVue.$store);
  homePageVue.$store.commit('setUserName', context.data.user)
  homePageVue.$store.commit('setShowMessage', context.data.showMessage)
  homePageVue.$store.commit('setPageMessage', context.data.pageMessage)
  homePageVue.$store.commit('setPermissions', context.data.permissions)

})(DMP_CONTEXT.get()))

