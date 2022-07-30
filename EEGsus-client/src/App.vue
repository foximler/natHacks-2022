<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <div class="flex w-100 pb-5">
<nav class="navbar navbar-expand-lg navbar-light bg-light ps-3 pe-3">
  <div class="pe-3" style="display: inline-flex;">
    <img alt="Brain Check" class="logo" src="@/assets/logo.png" width="25"/>
    <h3 style="color: hsla(160, 100%, 37%, 1)" class="ps-2">BrainCheck</h3>
  </div>
        <RouterLink to="/" class="p-3 rounded" :class="{active:$route.name =='landing'}">Home</RouterLink> 
        <RouterLink to="/survey" class="p-3 rounded" :class="{active:$route.name=='survey'}">Survey</RouterLink>
      </nav>
    </div>
<RouterView />
</template>

<script>
  import { mapGetters, mapActions, mapMutations } from "vuex";

export default {
  name: "Job",
  components: { },
  beforeMount() {
  },
  data() {
    return {};
  },
  computed: {
  },
  methods: {
  },
};
</script>
<style>
  .active{
    background-color: hsla(160, 100%, 37%, 1);
    color: white;
    border: r;
  }

</style>