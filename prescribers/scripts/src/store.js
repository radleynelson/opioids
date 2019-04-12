import Vue from 'vue';
import Vuex from 'vuex';

import axios from 'axios';
axios.defaults.withCredentials = true

import VuexPersistence from 'vuex-persist'

Vue.use(Vuex);


export default new Vuex.Store({
  state:{
    userName: '',
    showMessage: false,
    pageMessage: '',
    prescribersList: [],
    permissions: [],
  },
  getters: {
    userName: state => state.userName,
    showMessage: state => state.showMessage,
    pageMessage: state => state.pageMessage,
    prescribersList: state => state.prescribersList,
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
    setPrescribersList(state, prescribersList){
      state.prescribersList = prescribersList
    },
    setPermissions(state, permissions){
      state.permissions = permissions;
    }
    
  },
  actions: {
    getPrescribers(context) {
      return axios.get('/prescribers/index.prescribers_list').then(res => {
        context.commit('setPrescribersList', res.data)
      }).catch(err => {
        console.log(err);
      })
    },


  },
  plugins:[new VuexPersistence().plugin]
});
