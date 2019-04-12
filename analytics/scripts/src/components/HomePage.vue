<template>
  <div class="app">
    <h1>Opioid Statistics Dashboard</h1>
    <b-spinner v-if='!kpisVisible' style="width: 4rem; height: 4rem;" label="Loading..."></b-spinner>
    <section>
      <div style="margin-top:15px;" v-if="kpis != null">
        <b-row>
          <b-col>
            <p>Mean Risk Rank</p>
          </b-col>
          <b-col>
            <p>100% Opioid Prescribers</p>
          </b-col>
          <b-col>
            <p>Percent Opioid Prescriptoins</p>
          </b-col>
          <b-col>
            <p>At Risk Prescribers</p>
          </b-col>
          <b-col>
            <p>At Risk Limit</p>
          </b-col>
        </b-row>
        <b-row style=" margin-bottom:30px;">
          <b-col class="bg-primary text-white">
            <h2>{{kpis.mean_risk_rank}}</h2>
          </b-col>
          <b-col class="bg-warning text-white">
            <h2>{{kpis.only_prescribing_opioids}}</h2>
          </b-col>
          <b-col class="bg-success text-white">
            <h2>{{kpis.opioid_ratio}}%</h2>
          </b-col>
          <b-col class="bg-danger text-white">
            <h2>{{kpis.prescribers_at_risk}}</h2>
          </b-col>
          <b-col class="bg-info text-white">
            <h2>{{kpis.upper_bound_risk_rank}}</h2>
          </b-col>
        </b-row>
      </div>
      <b-row>
        <b-col>
          <h3>Opioids Total Prescriptions</h3>
          <b-spinner v-if='!dataVisible' style="width: 4rem; height: 4rem;" label="Loading..."></b-spinner>
            <bar-chart
              v-if="dataVisible"
              :chartdata="Top5OpioidPrescribers"
              :options="options"
            />
        </b-col>
        <b-col>
          <h3>Top 5 Specialties</h3>
            <b-col>
              <b-spinner v-if='!showSpecialtiesChart' style="width: 4rem; height: 4rem;" label="Loading..."></b-spinner>
              <bar-chart
                v-if="showSpecialtiesChart"
                :chartdata="SpecialtiesChart"
                :options="options"
              />
            </b-col>
          </b-col>

      </b-row>
      <b-row>
        <b-col>
          <h3>Overdose Percentage By State</h3>
          <b-spinner v-if='!showStatesChart' style="width: 4rem; height: 4rem;" label="Loading..."></b-spinner>
            <horizontal-bar
              v-if="showStatesChart"
              :chartdata="StatesChart"
              :options="options"
            />
        </b-col>
        <b-col>
          <h3>Top Doctors Comparison</h3>
          <b-spinner v-if='!radarVisible' style="width: 4rem; height: 4rem;" label="Loading..."></b-spinner>
          <radar v-if="radarVisible" :chartData="SpiderChartData" />
          <b-row v-if="radarVisible">
            <b-col>
                  <p>Doctor 1</p>
                  <select  v-model="RadarPrescriber1" class="form-control" name="" id="">
                    <option :value="prescriber.id" :key="index" v-for="(prescriber, index) in topPrescribers">
                      {{prescriber.doctorid}}
                    </option>
                  </select>
                </b-col>
                <b-col>
                  <p>Doctor 2</p>
                  <select v-model="RadarPrescriber2" class="form-control" name="" id="">
                    <option :value="prescriber.id" :key="index" v-for="(prescriber, index) in topPrescribers">
                      {{prescriber.doctorid}}
                    </option>
                  </select>
                </b-col>
          </b-row>
        </b-col>
      </b-row>

    </section>
  </div>
</template>

<script>
import BarChart from './BarChart.vue'
import axios from 'axios';
import HorizontalBar from './HorizontalBar.vue'
import Radar from './RadarChart.vue';
axios.defaults.withCredentials = true;
export default {
  name: 'HomePage',
  components: {
    BarChart,
    HorizontalBar,
    Radar,
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      radarVisible: false,
      RadarPrescriber1: null,
      RadarPrescriber2: null,
      opioidsDrugData: null,
      kpis: null,
      kpisVisible: false,
      dataVisible: false,
      topSpecialties: null,
      radarChartData: {
          labels: ['FENTANYL', 'HYDROCODONE.ACETAMINOPHEN', 'OXYCODONE.ACETAMINOPHEN', 'OXYCONTIN', 'ACETAMINOPHEN.CODEINE',],
      datasets: [
        {
          label: 'Prescriber 1',
          backgroundColor: 'rgba(179,181,198,0.2)',
          borderColor: 'rgba(179,181,198,1)',
          pointBackgroundColor: 'rgba(179,181,198,1)',
          pointBorderColor: '#fff',
          pointHoverBackgroundColor: '#fff',
          pointHoverBorderColor: 'rgba(179,181,198,1)',
          data: [65, 59, 90, 81, 56]
        },
        {
          label: 'My Second dataset',
          backgroundColor: 'rgba(255,99,132,0.2)',
          borderColor: 'rgba(255,99,132,1)',
          pointBackgroundColor: 'rgba(255,99,132,1)',
          pointBorderColor: '#fff',
          pointHoverBackgroundColor: '#fff',
          pointHoverBorderColor: 'rgba(255,99,132,1)',
          data: [28, 48, 40, 19, 96]
        }
]
        },
        SpiderChartData: {
          labels: ['Risk Rank', 'Opioid Prescription Ratio', 'State Overdoses Ratio',],
      datasets: [
        {
          label: 'Prescriber 1',
          backgroundColor: 'rgba(179,181,198,0.2)',
          borderColor: 'rgba(179,181,198,1)',
          pointBackgroundColor: 'rgba(179,181,198,1)',
          pointBorderColor: '#fff',
          pointHoverBackgroundColor: '#fff',
          pointHoverBorderColor: 'rgba(179,181,198,1)',
          data: [65, 59, 90]
        },
        {
          label: 'Prescriber 2',
          backgroundColor: 'rgba(255,99,132,0.2)',
          borderColor: 'rgba(255,99,132,1)',
          pointBackgroundColor: 'rgba(255,99,132,1)',
          pointBorderColor: '#fff',
          pointHoverBackgroundColor: '#fff',
          pointHoverBorderColor: 'rgba(255,99,132,1)',
          data: [28, 48, 60]
        }
]
        },
      Top5OpioidPrescribers: {
        labels: [],
        datasets: [{
            label: '# of Times Prescribed',
            data: [],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(34,139,34, 0.2)',
                'rgba(128, 0, 0, 0.2)',
                'rgba(128, 128, 128, 0.2)',
                'rgba(0,255,255, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(34,139,34, 1)',
                'rgba(128, 0, 0, 1)',
                'rgba(128, 128, 128, 1)',
                'rgba(0,255,255, 1)'
            ],
            borderWidth: 1
        }]
    },
    showSpecialtiesChart: false,
    SpecialtiesChart: {
        labels: [],
        datasets: [{
            label: 'Total Opioid Prescriptions',
            data: [],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(34,139,34, 0.2)',
                'rgba(128, 0, 0, 0.2)',
                'rgba(128, 128, 128, 0.2)',
                'rgba(0,255,255, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(34,139,34, 1)',
                'rgba(128, 0, 0, 1)',
                'rgba(128, 128, 128, 1)',
                'rgba(0,255,255, 1)'
            ],
            borderWidth: 1
        }]
    },
    showStatesChart: false,
    StatesChart: {
        labels: [],
        datasets: [{
            label: 'State Overdose Percent',
            data: [],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(34,139,34, 0.2)',
                'rgba(128, 0, 0, 0.2)',
                'rgba(128, 128, 128, 0.2)',
                'rgba(0,255,255, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(34,139,34, 1)',
                'rgba(128, 0, 0, 1)',
                'rgba(128, 128, 128, 1)',
                'rgba(0,255,255, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        },
        responsive: true
    },
    topPrescribers: null,
  }
  },
  watch: {
    RadarPrescriber1(newValue, oldValue) {
      this.syncSpider()
      
    },
    RadarPrescriber2(newValue, oldValue) {
      this.syncSpider()
    }
  },
  created(){
    this.getKpis()
    this.getOpioids()
    this.getTopPrescribers()
    this.getTopSpecialties()
    this.getTopStates()
  },
  computed: {
    userName() {
      return this.$store.getters.userName
    }
  },
  methods: {
    getKpis(){
      axios.get('/analytics/index.getkpis').then(res => {
        this.kpis = res.data;
        this.kpisVisible = true;
      }).catch(err => {
        console.log(err);
      })
    },
    syncSpider(){
      axios.get('/analytics/index.getSpider/'+ this.RadarPrescriber1 + '/'+this.RadarPrescriber2).then(res => {
        let test = []
        let test2 = []

        test.push(res.data['risk-rank'])
        test.push(res.data.percent)
        test.push(res.data['state-percent'])

        console.log(test)

        test2.push(res.data['risk-rank2'])
        test2.push(res.data.percent2)
        test2.push(res.data['state-percent2'])

        this.radarVisible = true;
        
        this.SpiderChartData = {
          labels: ['Risk Rank', 'Opioid Prescription Ratio', 'State Overdoses Ratio',],
      datasets: [
        {
          label: res.data.doctorid,
          backgroundColor: 'rgba(179,181,198,0.2)',
          borderColor: 'rgba(179,181,198,1)',
          pointBackgroundColor: 'rgba(179,181,198,1)',
          pointBorderColor: '#fff',
          pointHoverBackgroundColor: '#fff',
          pointHoverBorderColor: 'rgba(179,181,198,1)',
          data: test
        },
        {
          label: res.data.doctorid2,
          backgroundColor: 'rgba(255,99,132,0.2)',
          borderColor: 'rgba(255,99,132,1)',
          pointBackgroundColor: 'rgba(255,99,132,1)',
          pointBorderColor: '#fff',
          pointHoverBackgroundColor: '#fff',
          pointHoverBorderColor: 'rgba(255,99,132,1)',
          data: test2
        }
]
        }

      }).catch(err => {
        console.log(err)
      })
    },

    getTopStates(){
      axios.get('/analytics/index.getTopStates').then(res => {
        res.data.forEach(item => {
          this.StatesChart.labels.push(item.state)
          this.StatesChart.datasets[0].data.push(item.percent)
        });
        this.showStatesChart = true;
      })
    },
    getTopSpecialties(){
      axios.get('/analytics/index.getTopSpecialtiesToalOpioids').then(res => {
        this.topSpecialties = res.data;

        res.data.forEach(item => {
          this.SpecialtiesChart.labels.push(item.prescribers__specialties__specialty)
          this.SpecialtiesChart.datasets[0].data.push(item.qty__sum)
        });

        this.showSpecialtiesChart = true
      })
    },
    getTopPrescribers(){
      axios.get('/analytics/index.getTop50Prescribers').then(res => {
        this.topPrescribers = res.data;
        this.RadarPrescriber1 = res.data[0].id;
        this.RadarPrescriber2 = res.data[16].id;
      })
    },
    getOpioids() {
      axios.get('/analytics/index.getOpioids').then(res => {
        this.opioidsDrugData = res.data;
        res.data.forEach(drug => {
          this.Top5OpioidPrescribers.labels.push(drug.opioids__drugname)
          this.Top5OpioidPrescribers.datasets[0].data.push(drug.qty__sum)
        });
        this.dataVisible = true;
        
      })
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
