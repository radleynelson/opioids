<template>
  <div class="app">
    <div class="homepage">
      <h1>Prescribers</h1>
      <b-spinner v-if="deleting" style="width: 4rem; height: 4rem;" label="Loading..."></b-spinner>

      <div>
        Sorting By: <b>{{ sortBy }}</b>, Sort Direction:
        <b>{{ sortDesc ? 'Descending' : 'Ascending' }}</b>
      </div>
       <b-pagination
      v-model="currentPage"
      :total-rows="rows"
      :per-page="perPage"
      aria-controls="my-table"
    ></b-pagination>
    <div style="text-align: left; max-width: 65px; padding-bottom: 5px;">
      <select class="custom-select" v-model="perPage" name="" id="">
        <option>25</option>
        <option>50</option>
        <option>100</option>
      </select>
      <div style="display: grid; grid-template: auto auto / auto auto; margin-top: 5px; grid-column-gap: 5px; margin-bottom: 10px;">
        <button v-if="dataLoaded && !deleting && dashboardPermissions" @click="ExportCSV" style="" class="btn btn-info">Download <i class="fas fa-file-csv"></i></button>
        <router-link v-if="dataLoaded && !deleting && crudPermissions" class="btn btn-success" :to="{ name: 'EditPrescriber', params: {id: 0}}">Add Prescriber</router-link>
      </div>
    </div>
    <div v-if="items.length > 0 && !deleting" style="margin:auto; max-width: 500px; padding-bottom: 15px; grid-template: 1fr/1fr 1fr 4fr; display: grid; grid-column-gap: 10px;">
        <button @click="filterSearch" class="btn btn-primary"> <i class="fas fa-search"></i></button>
        <button @click="clearFilterSearch" class="btn btn-danger"> <i class="fas fa-backspace"></i> </button>
        <input type="text" v-model.lazy="filterString" id='FilterText' class="form-control" aria-describedby="search" placeholder="Search">
    </div>
     <div v-if="searching">
        <b-spinner style="width: 4rem; height: 4rem;" label="Loading..."></b-spinner>
      </div>
       <b-table
        id="my-table"
        :responsive="true"
        :items="items"
        :per-page="perPage"
        :current-page="currentPage"
        :fields="fields"
        :sort-by.sync="sortBy"
        :sort-desc.sync="sortDesc"
        :filter='filterText'
        :striped = 'true'
        :bordered = 'true'
        @filtered="onFiltered"
        @context-changed="onSearch"
        v-if="items.length > 0 && !deleting"
      >

        <template slot="doctorid" slot-scope="data">
          <router-link :to="{ name: 'Prescriber', params: {id: data.item.id}}">
            {{data.item.doctorid}}
          </router-link>          
        </template>
        <template v-if="crudPermissions" slot="edit" slot-scope="data">
            <router-link class="related-drug-link" :to="{ name: 'EditPrescriber', params: {id: data.item.id}}"><i class="fas fa-edit"></i></router-link>
        </template>
        <template v-if="crudPermissions" slot="delete" slot-scope="data">
            <i style="cursor: pointer;" @click="deleteUser(data.item.id)" class="fas fa-trash-alt"></i>
        </template>
      
      </b-table>
      <div v-if="!dataLoaded">
        <b-spinner style="width: 4rem; height: 4rem;" label="Loading..."></b-spinner>
      </div>
     
      <b-pagination
      v-model="currentPage"
      :total-rows="rows"
      :per-page="perPage"
      aria-controls="my-table"
    ></b-pagination>
    <div style="text-align: left; max-width: 65px; padding-bottom: 5px;">
      <select class="custom-select" v-model="perPage" name="" id="">
        <option>25</option>
        <option>50</option>
        <option>100</option>
      </select>
    </div>
      
    </div>
  </div>
</template>

<script>
import { ExportToCsv } from 'export-to-csv';
import axios from 'axios'
axios.defaults.withCredentials = true;
export default {
  name: 'HomePage',
  data() {
      return {
        currentPage: 1,
        sortBy: 'risk_rank',
        deleting: false,
        perPage: 25,
        sortDesc: true,
        filterString: '',
        filterNumber: '',
        filterText: '',
        rows: 1,
        filterBool: '',
        searching: false,
        fields: [],

      }
    },
  computed: {
    userName() {
      return this.$store.getters.userName
    },
    dashboardPermissions(){
      return this.$store.getters.permissions.includes('admin.dashboard')
    },
    crudPermissions(){
      return this.$store.getters.permissions.includes('admin.crud')
    },
    items() {
      return this.$store.getters.prescribersList;
    },
    dataLoaded(){
      return this.$store.getters.prescribersList.length > 0
    },
    dataRows(){
      return this.$store.getters.prescribersList.length;
    },

  },
  created(){
    this.$store.dispatch('getPrescribers');
    this.checkPermissions();
  },
  mounted(){
    //this.rows = this.items.length;
  },
  watch: {
    dataRows(newValue, oldValue) {
      this.rows = newValue
    }
  },
  methods: {
    filterSearch(){
      this.searching = true;
      this.filterText = this.filterString;
    },
    clearFilterSearch(){
      this.filterText = ''
      this.filterString = ''
    },
    onSearch(){
      //this.searching = true;
    },
    deleteUser(pid){
      if(confirm('Are you sure you want to delete? This can not be undone' + pid)){
        this.deleting = true
        axios.get('/prescribers/index.delete_prescriber/' + pid).then(res => {
          console.log(res.data)
          //this.$store.commit('setPageMessage', 'Deleted Successfully');
          this.$router.go()
        }).catch(err => {
            console.log('An error occured')
        })
      }
    },
    onFiltered(filteredItems) {
        this.rows = filteredItems.length
        this.currentPage = 1
        this.searching = false;
        console.log('testing')
      },
      ExportCSV(){
        let data = this.items;

        const options = { 
          fieldSeparator: ',',
          quoteStrings: '"',
          decimalSeparator: '.',
          showLabels: true, 
          showTitle: true,
          title: 'My Awesome CSV',
          useTextFile: false,
          useBom: true,
          useKeysAsHeaders: true,
          // headers: ['Column 1', 'Column 2', etc...] <-- Won't work with useKeysAsHeaders present!
        };
 
        const csvExporter = new ExportToCsv(options);
 
        csvExporter.generateCsv(data);
      },
      checkPermissions(){
        if(this.$store.getters.permissions.includes('admin.see_names')){
          this.fields = [
          { key: 'doctorid', label: 'Doctor Id', sortable: true },
          { key: 'fname', label: 'First Name', sortable: true },
          { key: 'lname', label: 'Last Name', sortable: true },
          { key: 'gender', label: 'Gender', sortable: true },
          { key: 'overdoses__abbrev', label: 'State', sortable: true },
          { key: 'credentials', label: 'Credentials', sortable: true },
          { key: 'risk_rank', label: 'Risk Rank', sortable: true },
          { key: 'isoutlier', label: 'Over Prescriber', sortable: true },
          { key: 'totalprescriptions', label: 'Total Prescriptions', sortable: true },
          { key: 'numberofopioidsprescribed', label: 'Opioids Prescribed', sortable: true },
          { key: 'specialties__specialty', label: 'Specialty', sortable: true }
        ]
        }
        else{
          this.fields = [
          { key: 'doctorid', label: 'Doctor Id', sortable: true },
          { key: 'gender', label: 'Gender', sortable: true },
          { key: 'overdoses__abbrev', label: 'State', sortable: true },
          { key: 'credentials', label: 'Credentials', sortable: true },
          { key: 'risk_rank', label: 'Risk Rank', sortable: true },
          { key: 'isoutlier', label: 'Over Prescriber', sortable: true },
          { key: 'totalprescriptions', label: 'Total Prescriptions', sortable: true },
          { key: 'numberofopioidsprescribed', label: 'Opioids Prescribed', sortable: true },
          { key: 'specialties__specialty', label: 'Specialty', sortable: true }
        ]
        }

        if (this.crudPermissions){
          this.fields.push({ key: 'edit', label: 'Edit', sortable: false })
          this.fields.push({ key: 'delete', label: 'Delete', sortable: false })
        }
      }
  },
  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.related-drug-link{
    color: black;
    text-decoration: none;
}
.related-drug-link:hover{
    text-decoration: underline;
}
.add-link{
  color: white;
  text-decoration: none;
}
.add-link:hover{
  color: white;
  text-decoration: none;
}

.button-box {
  text-align:center;
  margin-top:20px;
 }
</style>
