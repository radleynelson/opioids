// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue";
import VueRouter from "vue-router";
import App from "./src/App.vue";

// router setup
import routes from "./src/routes/routes";

// Plugins
import GlobalComponents from "./src/globalComponents";
import GlobalDirectives from "./src/globalDirectives";
import Notifications from "./src/components/NotificationPlugin";

// MaterialDashboard plugin
import MaterialDashboard from "./src/material-dashboard";

import Chartist from "chartist";

// configure router
const router = new VueRouter({
  routes, // short for routes: routes
  linkExactActiveClass: "nav-item active"
});

Vue.prototype.$Chartist = Chartist;

Vue.use(VueRouter);
Vue.use(MaterialDashboard);
Vue.use(GlobalComponents);
Vue.use(GlobalDirectives);
Vue.use(Notifications);

/* eslint-disable no-new */

console.log(routes);

window.addEventListener('load', function () {
  new Vue({
    el: "#app",
    render: h => h(App),
    router,
    data: {
      Chartist: Chartist
    }
  });
  
  console.log(Vue);
})


(function(context) {
    
  // utc_epoch comes from index.py
  console.log('Current epoch in UTC is ' + context.utc_epoch);
  
})(DMP_CONTEXT.get());



