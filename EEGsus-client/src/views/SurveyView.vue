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
   
    <div class="pe-2 col-md-6">
    <button class="btn w-100 btn-weirdgreen justify-content-center" @click="incrementForm(0)"><h2><font-awesome-icon icon="fa-solid fa-arrow-left"/> Back</h2></button>
  </div>
  <div class="pe-2 col-md-6">
    <button class="btn w-100 btn-weirdgreen justify-content-center" @click="incrementForm(1)"><h2>Begin Survey  <font-awesome-icon icon="fa-solid fa-arrow-right" /></h2></button>
  </div>
  </div>
  </div>
   <!-- ############### END OF HARDWARE INFO #################### -->
   <!-- Survey Page 1 -->
   <div class="pe-2 col-md-6" v-if="form.index==2">
    <div class="row g-3">
  <WelcomeItem>
    <template #icon>
    <font-awesome-icon icon="fa-solid fa-bullseye" />
    </template>
    <template #heading>Confidence</template>
    <b style="color:orange">fair</b>, the model is reporting 59% confidence.
  </WelcomeItem>
   <WelcomeItem>
    <template #icon>
    <font-awesome-icon icon="fa-solid fa-clock" />
    </template>
    <template #heading>Time</template>
    Please visualize each anwser for one second.
  </WelcomeItem>
<h2 class="text-center p-3">How are you feeling today?</h2>
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
    <div class="flex-justify text-center p-5 row">
    <div class="pe-2 col-md-6">
    <button class="btn w-100 btn-weirdgreen justify-content-center" @click="incrementForm(0)"><h2><font-awesome-icon icon="fa-solid fa-arrow-left"/> Back <font-awesome-icon icon="fa-solid fa-0"/></h2></button>
  </div>
  <div class="pe-2 col-md-6">
    <button class="btn w-100 btn-weirdgreen justify-content-center" @click="incrementForm(1)"><h2>Next Question <font-awesome-icon icon="fa-solid fa-9"/>  <font-awesome-icon icon="fa-solid fa-arrow-right" /></h2></button>
  </div>
  </div>
  </div>
    <!-- ############### END OF Survey pg 1 #################### -->
       <!-- Survey Page 2 -->
   <div class="pe-2 col-md-6" v-if="form.index==3">
    <div class="row g-3">
  <WelcomeItem>
    <template #icon>
    <font-awesome-icon icon="fa-solid fa-bullseye" />
    </template>
    <template #heading>Confidence</template>
    <b style="color:orange">fair</b>, the model is reporting 59% confidence.
  </WelcomeItem>
   <WelcomeItem>
    <template #icon>
    <font-awesome-icon icon="fa-solid fa-clock" />
    </template>
    <template #heading>Time</template>
    Please visualize each anwser for one second.
  </WelcomeItem>
<h2 class="text-center p-3">How would you rate your sleep recently?</h2>
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
    <div class="flex-justify text-center p-5 row">
    <div class="pe-2 col-md-6">
    <button class="btn w-100 btn-weirdgreen justify-content-center" @click="incrementForm(0)"><h2><font-awesome-icon icon="fa-solid fa-arrow-left"/> Back <font-awesome-icon icon="fa-solid fa-0"/></h2></button>
  </div>
  <div class="pe-2 col-md-6">
    <button class="btn w-100 btn-weirdgreen justify-content-center" @click="incrementForm(1)" ><h2>Next Question <font-awesome-icon icon="fa-solid fa-9" class="border" />  <font-awesome-icon icon="fa-solid fa-arrow-right" /></h2></button>
  </div>
  </div>
  </div>
    <!-- ############### END OF Survey pg 2 #################### -->
       <!-- Survey Page 3-->
   <div class="pe-2 col-md-6" v-if="form.index==4">
    <div class="row g-3">
  <WelcomeItem>
    <template #icon>
    <font-awesome-icon icon="fa-solid fa-bullseye" />
    </template>
    <template #heading>Confidence</template>
    <b style="color:orange">fair</b>, the model is reporting 59% confidence.
  </WelcomeItem>
   <WelcomeItem>
    <template #icon>
    <font-awesome-icon icon="fa-solid fa-clock" />
    </template>
    <template #heading>Time</template>
    Please visualize each anwser for one second.
  </WelcomeItem>
<h2 class="text-center p-3">How are you feeling today?</h2>
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
    <div class="flex-justify text-center p-5 row">
    <div class="pe-2 col-md-6">
    <button class="btn w-100 btn-weirdgreen justify-content-center" @click="incrementForm(0)"><h2><font-awesome-icon icon="fa-solid fa-arrow-left"/> Back <font-awesome-icon icon="fa-solid fa-0"/></h2></button>
  </div>
  <div class="pe-2 col-md-6">
    <button class="btn w-100 btn-weirdgreen justify-content-center" @click="incrementForm(1)"><h2>Next Question <font-awesome-icon icon="fa-solid fa-9"/>  <font-awesome-icon icon="fa-solid fa-arrow-right" /></h2></button>
  </div>
  </div>
  </div>
    <!-- ############### END OF Survey pg 4 #################### -->
       <!-- Survey Page 4 -->
   <div class="pe-2 col-md-6" v-if="form.index==5">
    <div class="row g-3">
  <WelcomeItem>
    <template #icon>
    <font-awesome-icon icon="fa-solid fa-bullseye" />
    </template>
    <template #heading>Confidence</template>
    <b style="color:orange">fair</b>, the model is reporting 59% confidence.
  </WelcomeItem>
   <WelcomeItem>
    <template #icon>
    <font-awesome-icon icon="fa-solid fa-clock" />
    </template>
    <template #heading>Time</template>
    Please visualize each anwser for one second.
  </WelcomeItem>
<h2 class="text-center p-3">How are you feeling today?</h2>
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
    <div class="flex-justify text-center p-5 row">
    <div class="pe-2 col-md-6">
    <button class="btn w-100 btn-weirdgreen justify-content-center" @click="incrementForm(0)"><h2><font-awesome-icon icon="fa-solid fa-arrow-left"/> Back <font-awesome-icon icon="fa-solid fa-0" class="border"/></h2></button>
  </div>
  <div class="pe-2 col-md-6">
    <button class="btn w-100 btn-weirdgreen justify-content-center" @click="incrementForm(1)"><h2>Next Question <font-awesome-icon icon="fa-solid fa-9" class="border"/>  <font-awesome-icon icon="fa-solid fa-arrow-right" /></h2></button>
  </div>
  </div>
  </div>
    <!-- ############### END OF Survey pg 4 #################### -->
      <!-- ############### Begin Final Buttons  #################### -->
<div class="pe-2 col-md-6" v-if="form.index==6">
    <div class="flex-justify text-center p-5 row">
   
    <div class="pe-2 col-md-6">
    <button class="btn w-100 btn-weirdgreen justify-content-center" @click="incrementForm(0)"><h2><font-awesome-icon icon="fa-solid fa-arrow-left"/> Back</h2></button>
  </div>
  <div class="pe-2 col-md-6">
    <button class="btn w-100 btn-weirdgreen justify-content-center" @click="incrementForm(1)"><h2>Save Results  <font-awesome-icon icon="fa-solid fa-download" /></h2></button>
  </div>
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
  name: "Job",
  components: { },
  beforeMount() {
  },
  sockets: {
        connect: function () {
            console.log('socket connected')
        },
        customEmit: function (data) {
            console.log('this method was fired by the socket server. eg: io.emit("customEmit", data)')
        }
    },
  data() {
    return {
      webSocket:{
        intput:1
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
    incrementForm(val){
      switch(val){
        case 0:
          this.form.index -=1
          break;
        case 1:
          this.form.index +=1
          break;
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