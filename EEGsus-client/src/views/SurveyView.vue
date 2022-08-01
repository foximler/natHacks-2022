<script setup>
import WelcomeItem from '../components/WelcomeItem.vue'
import DocumentationIcon from '../components/icons/IconDocumentation.vue'
import ToolingIcon from '../components/icons/IconTooling.vue'
import EcosystemIcon from '../components/icons/IconEcosystem.vue'
import CommunityIcon from '../components/icons/IconCommunity.vue'
import SupportIcon from '../components/icons/IconSupport.vue'
</script>

<template>
  <div class="d-flex justify-content-center">
    <!-- Patient Intake Form -->
<div class="col-md-6" v-if="form.index==0">
  <h1 class="text-center pb-5" style="color:white">Patient Info</h1>
    <div class="row g-3">
  <div class="col-md-6">
    <label for="inputfname" class="form-label">First Name</label>
    <input type="text" v-model="form.patientInfo.fName" class="form-control" id="inputfname" placeholder="John">
  </div>
  <div class="col-md-6">
    <label for="inputlname" class="form-label">Last Name</label>
    <input type="text"  v-model="form.patientInfo.lName" class="form-control" id="inputlname" placeholder="Doe">
  </div>
  <div class="col-12">
    <label for="inputPatientId" class="form-label">Patient Id</label>
    <input type="text"  v-model="form.patientInfo.ptnId" class="form-control" id="inputPatientId">
  </div>
  <div class="col-12">
    <label for="inputTestDate" class="form-label">Survey Date</label>
    <input type="date"  v-model="form.patientInfo.svyDate" class="form-control" id="inputTestDate">
  </div>
  </div>
  <div class="flex-justify text-center p-5">
    <button class="btn w-75 btn-weirdgreen justify-content-center" @click="incrementForm(1)"><h2>Begin Hardware Test  <font-awesome-icon icon="fa-solid fa-arrow-right" class="ps-2" /></h2></button>
  </div>
  </div>
  <!-- ############### END OF PATIENT INTAKE #################### -->
  <!-- Begin Hardware Info-->
  <div class="col-md-6" v-if="form.index==1">
  <h1 class="text-center pb-5" style="color:white">Hardware Status</h1>
    <div class="row g-3">
  <WelcomeItem>
    <template #icon>
    <font-awesome-icon icon="fa-solid fa-signal" />
    </template>
    <template #heading>Device Signal</template>
    <b style="color:green">Good</b>, we can see the device a-ok.
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <font-awesome-icon icon="fa-solid fa-server" />
    </template>
    <template #heading>Server Connection</template>
    <b style="color:green">Good</b>, we are having no issues talking to the server.
  </WelcomeItem>


  <WelcomeItem>
    <template #icon>
      <font-awesome-icon icon="fa-solid fa-microchip" />
    </template>
    <template #heading>AI Status</template>
    <b style="color:green">Good</b>, the brains behind the operation are behaving as expected.
  </WelcomeItem>
  </div>
  <div class="flex-justify text-center p-5 row">
   <div class="p-5 col-md-12">
    <button class="btn w-100 btn-weirdgreen justify-content-center" @click="playSound()"><h2><font-awesome-icon icon="fa-solid fa-play"/> Play Instructions</h2></button>
  </div>
    <div class="pe-2 col-md-6">
    <button class="btn w-100 btn-weirdgreen justify-content-center" @click="incrementForm(0)"><h2><font-awesome-icon icon="fa-solid fa-arrow-left"/> Back</h2></button>
  </div>
  <div class="pe-2 col-md-6">
    <button class="btn w-100 btn-weirdgreen justify-content-center" @click="incrementForm(1)"><h2>Begin Survey  <font-awesome-icon icon="fa-solid fa-arrow-right" /></h2></button>
  </div>
  </div>
  </div>
   <!-- ############### END OF HARDWARE INFO #################### -->
       <!-- Survey Page 4 -->
   <div class="pe-2 col-md-6" v-if="form.index >=2 && form.index<11">
    <div class="row g-3">
  <WelcomeItem>
    <template #icon>
    <font-awesome-icon icon="fa-solid fa-bullseye" />
    </template>
    <template #heading>Confidence</template>
    the model is reporting {{webSocket.confidence*100}}% confidence.
  </WelcomeItem>
<h2 class="text-center p-3" v-if="form.index==2">How would you rate your quality of life?</h2>
<h2 class="text-center p-3" v-if="form.index==3">How satisfied are you with your health?</h2>
<h2 class="text-center p-3" v-if="form.index==4">To what extent do you feel that physical pain prevents you from doing what you need to do?</h2>
<h2 class="text-center p-3" v-if="form.index==5">How much do you enjoy life?</h2>
<h2 class="text-center p-3" v-if="form.index==6">To what extent do you feel your life to be meaningful?</h2>
<h2 class="text-center p-3" v-if="form.index==7">How well are you able to concentrate?</h2>
<h2 class="text-center p-3" v-if="form.index==8">How healthy is your physical environment?</h2>
<h2 class="text-center p-3" v-if="form.index==9">How satisfied are you with yourself?</h2>
<h2 class="text-center p-3" v-if="form.index==10">How satisfied are you with the care you are recieving?</h2>

 <WelcomeItem :class="{active:webSocket.intput==1}">
    <template #icon>
    <font-awesome-icon icon="fa-solid fa-1" />
    </template>
    <template #heading> Very Bad</template>
  </WelcomeItem>
   <WelcomeItem :class="{active:webSocket.intput==2}">
    <template #icon>
    <font-awesome-icon icon="fa-solid fa-2" />
    </template>
    <template #heading>Bad</template>
  </WelcomeItem>
   <WelcomeItem :class="{active:webSocket.intput==3}">
    <template #icon>
    <font-awesome-icon icon="fa-solid fa-3" />
    </template>
    <template #heading>Fair</template>
  </WelcomeItem>
   <WelcomeItem :class="{active:webSocket.intput==4}">
    <template #icon>
    <font-awesome-icon icon="fa-solid fa-4" />
    </template>
    <template #heading>Good</template>
  </WelcomeItem>
     <WelcomeItem :class="{active:webSocket.intput==5}">
    <template #icon>
    <font-awesome-icon icon="fa-solid fa-5" />
    </template>
    <template #heading>Very Good</template>
  </WelcomeItem>
</div>
    <div class="flex-justify text-center p-1 row">
    <div class="pe-2 col-md-12">
    <button class="btn w-100 btn-weirdgreen justify-content-center" @click="playSound()"><h2><font-awesome-icon icon="fa-solid fa-play"/> Play Question Sound</h2></button>
  </div>
  </div>
    <div class="flex-justify text-center p-2 row">
    <div class="pe-2 col-md-6">
    <button class="btn w-100 btn-weirdgreen justify-content-center" @click="incrementForm(0)"><h2><font-awesome-icon icon="fa-solid fa-arrow-left"/> Back</h2></button>
  </div>
  <div class="pe-2 col-md-6">
    <button class="btn w-100 btn-weirdgreen justify-content-center" @click="incrementForm(1)"><h2>Next Question  <font-awesome-icon icon="fa-solid fa-arrow-right" /></h2></button>
  </div>
  </div>

  </div>
    <!-- ############### END OF Survey pg 4 #################### -->
      <!-- ############### Begin Final Buttons  #################### -->
      <div class="pe-2 col-md-6" v-if="form.index==11">
        <h2 class="p-5">The survey is complete and the patient can have the sensors removed.</h2>
    <button class="btn w-100 btn-weirdgreen justify-content-center" @click="saveData()"><h2>Save Details  <font-awesome-icon icon="fa-solid fa-download" /></h2></button>
    <div class="p-5">
    <button class="btn w-100 btn-danger justify-content-center" @click="form.index=0"><h2>Reset Form </h2></button>
  </div>
  </div>
</div>
</template>
<style>
</style>
<script>
  import { mapGetters, mapActions, mapMutations } from "vuex";
import { io } from "socket.io-client";

const socket = io("localhost:3000");

export default {
  name: "controller",
  beforeMount() {
    socket.on("wsUpdate", (data) => {
            this.webSocket = data
        });
  },
  data() {
    return {
      webSocket:{
        intput:1,
        confidence:0,
      },
      form:{
      index:0,
      patientInfo:{
        fName: '',
        lName: '',
        ptnId: null,
        svyDate: Date
      },
      surveyData:[],
    }
    };
  },
  computed: {
  },
  methods: {
    saveData(){
      const data = JSON.stringify(this.form)
    const blob = new Blob([data], {type: 'text/plain'})
    const e = document.createEvent('MouseEvents'),
    a = document.createElement('a');
    a.download = "test.json";
    a.href = window.URL.createObjectURL(blob);
    a.dataset.downloadurl = ['text/json', a.download, a.href].join(':');
    e.initEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
    a.dispatchEvent(e);
    },
    incrementForm(val){
      switch(val){
        case 0:
            socket.emit("changePage",this.form.index)
            this.form.index -=1
            this.form.surveyData.pop()
            break;
        case 1:
            socket.emit("changePage",this.form.index)
            this.form.index +=1
            this.form.surveyData.push({value:this.webSocket.intput,confidence:this.webSocket.confidence})
            break;
      }
    },
    playSound(){
      if (this.form.index == 11|| this.form.index ==1){
        switch(this.form.index){
          case 1:
           socket.emit("playSentence",'intro')
           break;
           case 11:
           socket.emit("playSentence",'final')
           break;
        }
      }
      else{
        socket.emit("playSound",this.form.index) 
      }
    }
  },
};
</script>

<style>
  .btn-weirdgreen{
    background-color: hsla(160, 100%, 37%, 1) !important;
    color: white;
  }
  .active{
    background-color: hsla(160, 100%, 37%, 1) !important;
    border-radius: 100px;
    background-size: 100% 50%;
    color: white;
  }
  .border{
    border-radius: 10px;
    border: 5px solid;
    width:35px;
    height: 35px; 
    padding-left:3px;
    padding-right:3px;
  }
</style>