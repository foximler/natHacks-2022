<template>
    <div class="d-flex justify-content-center white">
        <!-- Patient Intake Form -->
        <div class="col-md-12 text-center">
            <h1 class="vcenter">
                <font-awesome-icon @click="setInt(1)" icon="fa-solid fa-1" class="p-5" :class="{selected:webSocket.intput==1}"/>
                <font-awesome-icon @click="setInt(2)" icon="fa-solid fa-2" class="p-5" :class="{selected:webSocket.intput==2}"/>
                <font-awesome-icon @click="setInt(3)" icon="fa-solid fa-3" class="p-5" :class="{selected:webSocket.intput==3}"/>
                <font-awesome-icon @click="setInt(4)" icon="fa-solid fa-4" class="p-5" :class="{selected:webSocket.intput==4}"/>
                <font-awesome-icon @click="setInt(5)" icon="fa-solid fa-5" class="p-5" :class="{selected:webSocket.intput==5}"/>
            </h1>
        </div>
    </div>
</template>
<style>
</style>
<script>
import { mapGetters, mapActions, mapMutations } from "vuex";
import { io } from "socket.io-client";

function wait(ms) {
    var start = new Date().getTime();
    var end = start;
    while (end < start + ms) {
        end = new Date().getTime();
    }
}
const socket = io("localhost:3000");

function play(url) {
    return new Promise(function(resolve, reject) { // return a promise
        var audio = new Audio(); // create audio wo/ src
        audio.preload = "auto"; // intend to play through
        audio.autoplay = true; // autoplay when loaded
        audio.onerror = reject; // on error, reject
        audio.onended = resolve; // when done, resolve

        audio.src = url
    });
}
export default {
    name: "Job",
    components: {},
    beforeMount() {
        socket.on("wsUpdate", (data) => {
            this.webSocket = data
        });
    },
    data() {
        return {
            webSocket: {
                intput: null,
                confidence:null
            },
            form: {
                index: 0,
                patientInfo: {
                    fName: '',
                    lName: '',
                    ptnId: null,
                    svyDate: Date
                },
                surveyData: [],
            }
        };
    },
    computed: {},
    methods: {
        setInt(data){
            socket.emit("feedModel",data)
        }
    },
};
</script>
<style>
.vcenter {
    margin-top: 20%;
}

.white {
    color: white;

}
.selected {
    color: green;
}

</style>