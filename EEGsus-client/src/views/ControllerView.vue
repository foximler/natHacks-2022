<template>
    <div class="d-flex justify-content-center white">
        <!-- Patient Intake Form -->
        <div class="col-md-6 text-center pt-5">
            <h3>Please focus on the cross and follow the auditory cues.</h3>
            <h1 class="vcenter">
                <font-awesome-icon icon="fa-solid fa-plus" class="p-5" />
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
        socket.on("indexPlay", (data) => {
            play(`/${data}.wav`).then(function() {
                wait(1500)
                play('/beep.wav')
            })
        });
        socket.on("instructionPlay", (data) => {
            play(`/${data}.wav`)
        });
    },
    data() {
        return {
            webSocket: {
                intput: 1
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
    methods: {},
};
</script>
<style>
.vcenter {
    margin-top: 25%;
}

.white {
    color: white;

}
</style>