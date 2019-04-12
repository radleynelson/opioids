<template>
  <div class="app">
    <div class="homepage">
      <b-jumbotron bg-variant="dark" text-variant="white" border-variant="dark">
        <template slot="header">
          <div style="width: 35%; margin: auto;">
            <img style="width: 100%" src='/static/homepage/media/HHS-Logo white.png' alt="Our Logo">
          </div>
        </template>

        <template slot="lead">
         
        </template>

        <hr class="my-4">

        <div style="width: 75%; margin: auto;">
          <h5>
            The United States has a major opioid crisis, with the number of overdoses on the rise it is critical we find a solution to safe prescribing of these powerful drus.
          </h5>
        </div>
      </b-jumbotron>

      <b-card-group deck>
        <b-card title="Drugs" img-src="https://owips.com/sites/default/files/styles/225x120/public/clipart/medicine-clipart/278919/medicine-clipart-278919-1536229.jpg?itok=IIk-QIzg" img-alt="Image" img-top>
          <b-card-text>
            View, explore, filter and search our database of 250 drugs
            <div style="margin-top:15px">
              <a class="btn btn-success" href="/drugs">View Drugs</a>
            </div>
          </b-card-text>
        </b-card>
        <b-card title="" img-src="http://www.ubalt.edu/merrick/uploads/660x450-mobile-homepage/660x450-Infographic%20Icons_Data%20Analytics.jpg" img-alt="Image" img-top>
          <b-card-text>
           The latest statistics indicate that the total yearly overdose deaths due to opioids reached a new high of 70,237 in 2017. In that same year, President Trump declared the opioid crisis a public health emergency. 

          </b-card-text>
        </b-card>
        <b-card title="Drug Prescribers" img-src="http://www.clker.com/cliparts/0/4/C/O/g/t/doctor-and-patient-blue.svg.hi.png" img-alt="Image" img-top>
         <b-card-text>
            Discover, analyze, search and sort our database of 25,000 drug prescribers
            <div style="margin-top: 15px;">
              <a class="btn btn-success" href="/prescribers">View Drug Prescribers</a>
            </div>
          </b-card-text>
        </b-card>

      </b-card-group>
    </div>
  </div>
</template>

<script>
import logo from '../images/logo2White.png'
export default {
  name: 'HomePage',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
    }
  },
  computed: {
    userName() {
      return this.$store.getters.userName
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
