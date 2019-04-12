import Vue from 'vue';
import Vuex from 'vuex';

import axios from 'axios';

import VuexPersistence from 'vuex-persist'

Vue.use(Vuex);


export default new Vuex.Store({
  state:{
    userName: '',
    showMessage: false,
    pageMessage: '',
    permissions: '',
  },
  getters: {
    userName: state => state.userName,
    showMessage: state => state.showMessage,
    pageMessage: state => state.pageMessage,
    permissions: state => state.permissions,

  },
  mutations: {
    setUserName (state, userName) {
      state.userName = userName;
    },
    setShowMessage (state, showMessage){
      state.showMessage = showMessage;
    },
    setPageMessage(state, pageMessage){
      state.pageMessage = pageMessage;
    },
    setPermissions(state, permissions){
      state.permissions = permissions
    }
    
  },
  actions: {
    getPosts(context) {
      return axios.get('http://rissanelson.com/wp-json/wp/v2/posts').then(res => {
        context.commit('setPosts', res.data)
      }).catch(err => {
        console.log(err);
      })
    },


  },
  plugins:[new VuexPersistence().plugin]
});
