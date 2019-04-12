<template>
    <div>
        <div v-if="dataVisible">
            <h1>{{this.userList.drug[0].drugname}}</h1>
            <div class="info-table">
                <b-table stacked :bordered=true :items="currentDrug"></b-table>
            </div>
        </div>
        
        <section v-if="permissions">
            <div class="container chart-container">
                <h3 v-if="dataVisible">Top 10 Prescribers of {{this.userList.drug[0].drugname}}</h3>
                <div v-if="!dataVisible" class="text-center">
                    <b-spinner style="width: 4rem; height: 4rem;" label="Loading..."></b-spinner>
                </div>
                <bar-chart
                    v-if="dataVisible"
                    :chartdata="chartdata"
                    :options="options"
                />
            </div>
        </section>
        <div v-if="!relatedItemsVisible" class="text-center">
            <b-spinner variant='primary' style="width: 4rem; height: 4rem;" label="Loading..."></b-spinner>
        </div>
        <div v-if="relatedItemsVisible">
            <h2>Related Drugs</h2>
                <div>
                    <table class="table">
                        <thead>
                            <tr>
                                <th>Drug Name</th>
                                <th>Times Prescirbed</th>
                                <th>Is Opioid</th>
                                <th>Risk Score</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr :key="idx" v-for="(data, idx) in relatedItems">
                                <td><router-link class="related-drug-link" :to="{ name: 'Drug', params: {id: data.id}}">{{data.drugname}}</router-link></td>
                                <td>{{data.total_prescriptions}}</td>
                                <td>{{data.isopioid == 1 ? 'Yes' : 'No'}}</td>
                                <td>{{data.risk_score}}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
    </div>
</template>

<script>
    import axios from 'axios';
    axios.defaults.withCredentials = true;
    import BarChart from './BarChart.vue'
    export default {
        name: 'Drug',
        fields: ['Drug Id', 'Drug Name', 'Opioid', 'Total Times Prescribed'],
        components: { BarChart },
        data() {
            return {
                test: 3,
                relatedItems: [],
                relatedItemsVisible: false,
                currentDrug: [],
                userList: {},
                dataVisible: false,
                loaded: false,
                chartdata: {
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
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        },
         onClick: function(event, i){
              let e = i[0];
            console.log(e._index)
            var x_value = this.data.labels[e._index];
            var y_value = this.data.datasets[0].data[e._index];
            console.log(x_value);
            console.log(y_value);
         }
    }
            }
        },
        computed: {
            permissions() {
                return this.$store.getters.permissions.includes('admin.analytics') 
            },
            dashboardPermissions(){
                return this.$store.getters.permissions.includes('admin.dashboard') 
            },
        },
        created(){
            this.getData()
            this.getRelatedDrugs()
        },
        watch: {
            '$route' (to, from) {
                this.getData();
                this.getRelatedDrugs();
            }
        },
        methods: {
            getRandomInt () {
                return Math.floor(Math.random() * (50 - 5 + 1)) + 5
            },
            getData(){
                this.currentDrug = [],
                this.dataVisible = false;
                this.chartdata.labels = []
                this.chartdata.datasets[0].data = []
                axios.get('/drugs/index.drug/'+this.$route.params.id).then(res => {
                this.userList = res.data;
                if(this.$store.getters.permissions.includes('admin.analytics')){
                    res.data.userList.forEach(person => {
                    if(this.dashboardPermissions)
                        this.chartdata.labels.push(person.prescribers__fname + ' ' + person.prescribers__lname)
                    else
                        this.chartdata.labels.push(person.prescribers__doctorid)
                        
                    this.chartdata.datasets[0].data.push(person.qty)
                });
                }
                this.dataVisible = true;
                let drug = {};
                drug['Drug Id'] = res.data.drug[0].id;
                drug['Drug Name'] = res.data.drug[0].drugname;
                drug.Opioid = res.data.drug[0].isopioid == 1 ? 'Yes' : 'No';
                drug['Total Times Prescribed'] = res.data.drug[0].total_prescriptions;
                this.currentDrug.push(drug);
                
            }).catch(err => {
                console.log(err);
            })
            },
            getRelatedDrugs(){
                this.relatedItemsVisible = false
                axios.get('/drugs/index.related_drugs/' + this.$route.params.id).then(res => {
                    this.relatedItems = res.data;
                    this.relatedItemsVisible = true;
                }).catch(err => {
                    console.log(err);
                })
            }
        },
    }
</script>

<style scoped>
.chart-container{
    width: 45%;
}
.info-table{
    margin-bottom: 50px;
}
.card-container{
    display: grid;
    grid-template: auto auto auto auto auto/ auto auto auto auto auto;
    grid-column-gap: 5px;
}
.related-drug-link{
    color: black;
    text-decoration: none;
}
.related-drug-link:hover{
    text-decoration: underline;
}
</style>