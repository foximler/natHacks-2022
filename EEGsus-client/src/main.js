import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createStore } from 'vuex'

import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import { library } from '@fortawesome/fontawesome-svg-core'
/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faArrowRight, faSignal, faArrowLeft, faServer, faMicrochip, faDownload, faBullseye, fa1, fa2, fa3, fa4, fa5, fa6, fa7, fa8, fa9, fa0,faClock} from '@fortawesome/free-solid-svg-icons'
/* add icons to the library */
library.add(faArrowRight, faSignal, faArrowLeft, faServer, faMicrochip, faDownload, faBullseye, fa1, fa2, fa3, fa4, fa5, fa6, fa7, fa8, fa9, fa0, faClock)
import './assets/main.css'
//data for the app. we usually seperate this stuff but hackathon rules prevail over security and optimization
const store = createStore({
  state () {
    return {
    }
  },
  mutations: {
  }
})

const app = createApp(App)

app.use(router)
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(store)
app.mount('#app')
