<template>
    <div>
        <div v-if="!dataVisible">
            <b-spinner style="width: 4rem; height: 4rem;" label="Loading..."></b-spinner>
        </div>
        <div v-if="dataVisible">
            <h1>Doctor {{this.prescriberLeft[0]['Doctor Id']}}</h1>
            <div style="display:grid; grid-template: auto auto/auto auto;">
                <div class="info-table">
                    <b-table stacked :bordered=true :items="prescriberLeft"></b-table>
                </div>
                <div class="info-table">
                    <b-table stacked :bordered=true :items="prescriber"></b-table>
                </div>
            </div>
        </div>
        <section v-if='analyticsPermissions'>
            <div v-if="dataVisible">
                <h3>Analytics  <i class="fas fa-chart-bar"></i></h3>
                <b-tabs content-class="mt-3">
                    <b-tab title="Items" active>
                        <div class="container chart-container">
                            <h3 v-if="dataVisible">Top {{drugsInGraph}} Drugs Prescribers by Doctor {{this.prescriber[0]['Doctor Id']}}</h3>
                            <bar-chart
                            v-if="dataVisible"
                            :chartdata="chartdata"
                            :options="options"
                            />
                        </div>
                        <h4>All Drugs Prescribed by Doctor {{this.prescriber[0].doctorid}}</h4>
                        <b-table
                            id="my-table"
                            :items="prescriberDrugsList"
                            :fields="fields"
                            :per-page="perPage"
                            :current-page="currentPage"
                            :sort-by.sync="sortBy"
                            :sort-desc.sync="sortDesc"
                            :filter='filterText'
                            :striped = 'true'
                            :bordered = 'true'
                        >
                            <template slot="opioids__drugname" slot-scope="data">
                                <a class="related-drug-link" :href="'/drugs#/items/' + data.item.opioids__id">
                                    {{data.item.opioids__drugname}}
                                </a>
                            </template>
                            <template slot="opioids__isopioid" slot-scope="data">
                                {{data.item.opioids__isopioid == 1 ? 'Yes' : 'No'}}
                            </template>
                        </b-table>
                        <b-pagination
                        v-model="currentPage"
                        :total-rows="prescriberDrugsList.length"
                        :per-page="perPage"
                        aria-controls="my-table"
                        ></b-pagination>
                    </b-tab>
                    <b-tab title="Related Users">
                        <section>
                            <h2 style="margin-bottom: 25px" v-if="finalRelatedUsers.length > 1">Related Users</h2>
                            <div v-if="finalRelatedUsers.length < 1">
                                <b-spinner variant='info' style="width: 4rem; height: 4rem;" label="Loading..."></b-spinner>
                            </div>
                            <div :key='index' v-for="(user, index) in finalRelatedUsers">
                                <div style="display: grid; grid-template: auto auto / auto auto;">
                                    <div style="margin: auto;">
                                        <a class="related-drug-link" :href="'/prescribers#/items/' + user.Id">Doctor{{user['Doctor Id']}}</a>
                                    </div>
                                    <div>
                                        <table style="width:350px;" class="table table-striped table-bordered">
                                            <tbody>
                                                <tr>Top Prescribed Drugs</tr>
                                                <tr :key='index' v-for="(drugs, index) in user.Drugs">
                                                    <td><a class="related-drug-link" :href="'/drugs#/items/' + drugs.opioids__id">{{drugs.opioids__drugname}}</a></td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                        </section>
                    </b-tab>
                    <b-tab v-if="dashboardPermissions || this.currentUser" title="Reccomended Items">
                        <section>
                            <div v-if="!reccomendedItemsVisible">
                                <b-spinner variant='info' style="width: 4rem; height: 4rem;" label="Loading..."></b-spinner>
                            </div>
                            <div v-if="reccomendedItemsVisible">
                                <h3>Top 5 Opioid Alternatives</h3>
                                <b-table :fields="relatedDrugsFields" striped hover :items="reccomendedItems">
                                    <template slot="drugname" slot-scope="data">
                                        <a class="related-drug-link" :href="'/drugs#/items/' + data.item.id">
                                            {{data.item.drugname}}
                                        </a>
                                    </template>
                                </b-table>
                            </div>
                        </section>
                    </b-tab>
                </b-tabs>  
            </div>
        </section>
    </div>
</template>

<script>
    import axios from 'axios';
    axios.defaults.withCredentials = true;
    import BarChart from './BarChart.vue'
    export default {
        name: 'Prescirber',
        //fields: ['Drug Id', 'Drug Name', 'Opioid', 'Total Times Prescribed'],
        components: { BarChart },
        data() {
            return {
                test: 3,
                reccomendedItemsVisible: false,
                relatedItems: [],
                reccomendedItems:[],
                currentPage: 1,
                drugsInGraph: 5,
                sortBy: 'qty',
                relatedDrugsFields: [
          { key: 'drugname', label: 'Drug Name', sortable: true },
          { key: 'total_prescriptions', label: 'Number of Prescriptions', sortable: true },
          { key: 'risk_score', label: 'Risk Rank', sortable: true },
        ],
                sortDesc: true,
                filterText: '',
                relatedUsers: [],
                finalRelatedUsers:[],
                perPage: 10,
                fields: [
          { key: 'opioids__drugname', label: 'Drug Name', sortable: true },
          { key: 'qty', label: 'Number of Prescriptions', sortable: true },
          { key: 'opioids__isopioid', label: 'Is Opioid', sortable: true },
          { key: 'opioids__risk_score', label: 'Risk Score', sortable: true }
        ],
                relatedItemsVisible: false,
                prescriberDrugsList: [],
                prescriber: [],
                prescriberLeft: [],
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
             console.log(event)
             console.log(i)
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
            analyticsPermissions(){
                return this.$store.getters.permissions.includes('admin.analytics')
            },
            dashboardPermissions(){
                return this.$store.getters.permissions.includes('admin.dashboard')
            },
            currentUser(){
                if(this.prescriberLeft.length < 1)
                    return false;
                else
                    return this.$store.getters.userName == this.prescriberLeft[0]['Doctor Id'];
            }
        },
        created(){
            this.getData()
            this.getRelatedUsers()
        },
        watch: {
            '$route' (to, from) {
                this.reccomendedItemsVisible = false
                this.getData();
                this.getRelatedUsers();
                this.finalRelatedUsers = [];
            }
        },
        methods: {
            getRandomInt () {
                return Math.floor(Math.random() * (50 - 5 + 1)) + 5
            },
            getRelatedUsers(){
                axios.get('prescribers/index.related_prescribers/' + this.$route.params.id).then(res => {
                    this.relatedUsers = res.data;
                    this.relatedUsers.forEach(person => {
                        console.log(person)
                        this.finalRelatedUsers.push({
                            'Doctor Id': person.userInfo.doctorid,
                            'Id': person.userInfo.id,
                            Drugs: person.Top5Drugs
                        })
                    });
                })
            },
            getReccomendedItems(){
                axios.get('/prescribers/index.drug_reccomender/' + this.$route.params.id + '/' + this.prescriberDrugsList[0].opioids__id).then(res => {
                    this.reccomendedItems = res.data;
                    this.reccomendedItemsVisible = true;
                }).catch(err => {
                    console.log(err);
                })
            },
            getData(){
                this.dataVisible = false;
                this.chartdata.labels = []
                this.chartdata.datasets[0].data = []
                axios.get('/prescribers/index.prescriber/'+this.$route.params.id).then(res => {
                    let pdataLeft = {};
                    let pdata = {};
                    if(this.$store.getters.permissions.includes('admin.see_names')){
                            pdataLeft = {
                            'Doctor Id': res.data.PrescriberDataLeft[0].doctorid,
                            'First Name': res.data.PrescriberDataLeft[0].fname,
                            'Last Name': res.data.PrescriberDataLeft[0].lname,
                            'Total Prescriptions': res.data.PrescriberDataLeft[0].totalprescriptions,
                            'Opioids Prescribed': res.data.PrescriberDataLeft[0].numberofopioidsprescribed,
                            'Credentials': res.data.PrescriberDataLeft[0].credentials,
                        }
                        pdata = {
                            'Gender': res.data.PrescriberData[0].gender,
                            'State': res.data.PrescriberData[0].overdoses__abbrev,
                            'Specialty': res.data.PrescriberData[0].specialties__specialty,
                            'Opioid Prescriber': res.data.PrescriberData[0].opioid_prescriber == 1 ? 'Yes': 'No',
                            'Risk Rank': res.data.PrescriberData[0].risk_rank,
                            'High Risk': res.data.PrescriberData[0].isoutlier == true ? 'Yes': 'No'
                        }
                    }
                    else{
                        pdataLeft = {
                            'Doctor Id': res.data.PrescriberDataLeft[0].doctorid,
                            'Total Prescriptions': res.data.PrescriberDataLeft[0].totalprescriptions,
                            'Opioids Prescribed': res.data.PrescriberDataLeft[0].numberofopioidsprescribed,
                            'Credentials': res.data.PrescriberDataLeft[0].credentials,
                            'Gender': res.data.PrescriberData[0].gender,

                        }
                        pdata = {
                            'State': res.data.PrescriberData[0].overdoses__abbrev,
                            'Specialty': res.data.PrescriberData[0].specialties__specialty,
                            'Opioid Prescriber': res.data.PrescriberData[0].opioid_prescriber == 1 ? 'Yes': 'No',
                            'Risk Rank': res.data.PrescriberData[0].risk_rank,
                            'High Risk': res.data.PrescriberData[0].isoutlier == true ? 'Yes': 'No'
                        }
                    }
                    this.prescriber = [];
                    this.prescriberLeft = [];
                    this.prescriber.push(pdata);
                    this.prescriberLeft.push(pdataLeft);
                    this.prescriberDrugsList = res.data.drugs;

                    let countTo = res.data.drugs.length;
                    if (countTo > 10) 
                            countTo = 10;
                    
                    this.drugsInGraph = countTo

                    for (let i = 0; i < countTo; i++){
                        this.chartdata.labels.push(res.data.drugs[i].opioids__drugname);
                        this.chartdata.datasets[0].data.push(res.data.drugs[i].qty)
                    }
                    this.dataVisible = true;   
            }).then(res => {
                if(this.dashboardPermissions || this.currentUser){
                    this.getReccomendedItems()
                }

            }).catch(err => {
                console.log(err);
            })
            },
            
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