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
    drugsList: '',
    permissions: '',
  },
  getters: {
    userName: state => state.userName,
    showMessage: state => state.showMessage,
    pageMessage: state => state.pageMessage,
    drugsList: state => state.drugsList,
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
    setDrugsList(state, drugsList){
      state.drugsList = drugsList
    },
    setPermissions(state, permissions){
      state.permissions = permissions;
    }
    
  },
  actions: {
    getDrugs(context) {
      return axios.get('/drugs/index.drugs_list').then(res => {
        res.data.forEach(element => {
          if (element.isopioid == 1){
            element.isopioid = 'Yes'
          }
          else{
            element.isopioid = 'No'
          }
        });
        context.commit('setDrugsList', res.data)
      }).catch(err => {
        console.log(err);
      })
    },


  },
  plugins:[new VuexPersistence().plugin]
});
