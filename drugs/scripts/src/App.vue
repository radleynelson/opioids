<template>
  <div id="app">
    <div class="container">
      <b-alert v-if="showMessage" show dismissible fade>{{pageMessage}}</b-alert>
      <router-view/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  computed: {
    showMessage() {
      return this.$store.getters.showMessage
    },
    pageMessage(){
      return this.$store.getters.pageMessage
    }
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 10px;
}
</style>
