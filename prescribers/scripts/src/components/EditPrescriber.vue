<template>
    <div>
        <b-spinner v-if="!show" style="width: 4rem; height: 4rem;" label="Loading..."></b-spinner>
        <b-card v-if="show" :title="this.$route.params.id == 0 ? 'Add Prescriber' : 'Edit Prescriber' " class="mb-2" style="max-width: 500px; text-align:left; margin:auto">
                <b-form @reset="onReset" @submit="onSubmit" >
                <b-form-group
                    id="input-group-fname"
                    label="First Name:"
                    label-for="fname"
                    description="We'll never share your data with anyone else."
                >
                    <b-form-input
                    id="fname"
                    v-model="form.fname"
                    type="text"
                    required
                    placeholder="First Name"
                    ></b-form-input>
                </b-form-group>

                <b-form-group id="input-group-lname" label="Last Name:" label-for="lname">
                    <b-form-input
                    id="lname"
                    v-model="form.lname"
                    required
                    placeholder="Last Name"
                    ></b-form-input>
                </b-form-group>

                <b-form-group id="input-group-doctorid" label="Doctor Id:" label-for="doctorid">
                    <b-form-input
                    id="doctorid"
                    v-model="form.doctorid"
                    required
                    placeholder="Doctor Id"
                    ></b-form-input>
                </b-form-group>

                <b-form-group id="input-group-credentials" label="Credentials:" label-for="credentials">
                    <b-form-input
                    id="credentials"
                    v-model="form.credentials"
                    required
                    placeholder="Credentials"
                    ></b-form-input>
                </b-form-group>


                <b-form-group id="input-group-numberofopioidsprescribed" label="Total Opioids Prescribed:" label-for="numberofopioidsprescribed">
                    <b-form-input
                    id="numberofopioidsprescribed"
                    v-model="form.numberofopioidsprescribed"
                    required
                    placeholder="Total Opioids Prescribed"
                    ></b-form-input>
                </b-form-group>

                <b-form-group id="input-group-opioid_prescriber" label="Is Opioid Prescriber:" label-for="opioid_prescriber">
                    <b-form-input
                    id="opioid_prescriber"
                    v-model="form.opioid_prescriber"
                    required
                    placeholder="Is Opioid Prescriber"
                    ></b-form-input>
                </b-form-group>

                <b-form-group id="input-group-overdoses_id" label="State:" label-for="overdoses_id">
                    <b-form-input
                    id="overdoses_id"
                    v-model="form.overdoses_id"
                    required
                    placeholder="State"
                    ></b-form-input>
                </b-form-group>

                <b-form-group id="input-group-specialties_id" label="Speciality:" label-for="specialties_id">
                    <b-form-input
                    id="specialties_id"
                    v-model="form.specialties_id"
                    required
                    placeholder="Speciality"
                    ></b-form-input>
                </b-form-group>

                <b-form-group id="input-group-totalprescriptions" label="Total Prescriptions:" label-for="totalprescriptions">
                    <b-form-input
                    id="specialties_id"
                    v-model="form.totalprescriptions"
                    required
                    placeholder="Total Number of Prescriptions"
                    ></b-form-input>
                </b-form-group>

                <b-form-group id="input-group-gender" label="Gender:" label-for="gender">
                    <b-form-select
                    id="gender"
                    v-model="form.gender"
                    :options="gender"
                    required
                    ></b-form-select>
                </b-form-group>
                
                <b-button type="submit" variant="primary">Submit</b-button>
                <b-button type="reset" variant="danger">Reset</b-button>
            </b-form>
        </b-card>
        
    </div>
</template>

<script>
    import axios from 'axios'
    axios.defaults.withCredentials = true;

    export default {
        data() {
            return {
                prescriber: {},
                form: {
                    credentials: '',
                    doctorid: '',
                    fname: null,
                    lname: null,
                    gender: null,
                    numberofopioidsprescribed: null,
                    opioid_prescriber: null,
                    overdoses_id: null,
                    specialties_id: null,
                    totalprescriptions: null
                },
                gender: [{ text: 'Select One', value: null }, 'M', 'F'],
                show: false
            }
        },
        watch: {
            '$route' (to, from) {
                if(this.$route.params.id > 0){
                    this.getData();
                }
                else{
                    this.show = true;
                    this.form.credentials = "";
                    this.form.doctorid = "";
                    this.form.fname = "";
                    this.form.lname = "";
                    this.form.gender = null;
                    this.form.numberofopioidsprescribed = "";
                    this.form.opioid_prescriber = "";
                    this.form.overdoses_id = "";
                    this.form.specialties_id = "";
                    this.form.totalprescriptions = "";
                    this.show = false

                    this.$nextTick(() => {
                        this.show = true
                    })
                }
            }
        },
        methods: {
            onSubmit(evt) {
            evt.preventDefault()
            axios.post('/prescribers/index.update_prescriber/' + this.$route.params.id, this.form).then(res => {
                this.$store.commit('setPageMessage', res.data);
                if(res.data == 'Saved Successfully'){
                    this.$router.push({ name: 'name',})
                }
            }).catch(err => {
                console.log(err);
                this.$store.commit('setPageMessage', err);
            })
        },
            onReset(evt) {
                evt.preventDefault()
                this.form.credentials = "";
                this.form.doctorid = "";
                this.form.fname = "";
                this.form.lname = "";
                this.form.gender = null;
                this.form.numberofopioidsprescribed = "";
                this.form.opioid_prescriber = "";
                this.form.overdoses_id = "";
                this.form.specialties_id = "";
                this.form.totalprescriptions = "";
                this.show = false

                this.$nextTick(() => {
                    this.show = true
                })

        },
      getData(){
          this.show = false;
          
           axios.get('/prescribers/index.edit_prescriber/' + this.$route.params.id)
           .then(res => {
              this.prescriber = res.data[0];
          }).then(res => {
              this.bindData();
              this.show = true;
          }).catch(err => {
              console.log(err);
          })
      },
      bindData(){
          this.form.credentials = this.prescriber.credentials;
          this.form.doctorid = this.prescriber.doctorid;
          this.form.fname = this.prescriber.fname;
          this.form.lname = this.prescriber.lname;
          this.form.gender = this.prescriber.gender;
          this.form.numberofopioidsprescribed = this.prescriber.numberofopioidsprescribed;
          this.form.opioid_prescriber = this.prescriber.opioid_prescriber;
          this.form.overdoses_id = this.prescriber.overdoses_id;
          this.form.specialties_id = this.prescriber.specialties_id;
          this.form.totalprescriptions = this.prescriber.totalprescriptions;
      }
    },
    created () {
        if(this.$route.params.id > 0){
            this.getData();
            }
        else{
            this.show = true;
            this.form.credentials = "";
            this.form.doctorid = "";
            this.form.fname = "";
            this.form.lname = "";
            this.form.gender = null;
            this.form.numberofopioidsprescribed = "";
            this.form.opioid_prescriber = "";
            this.form.overdoses_id = "";
            this.form.specialties_id = "";
            this.form.totalprescriptions = "";
            this.show = false

            this.$nextTick(() => {
                this.show = true
            })
        }
      },
}
</script>

<style lang="scss" scoped>

</style>