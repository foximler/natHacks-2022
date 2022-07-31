<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from '../components/HelloWorld.vue'
import TheWelcome from '@/components/TheWelcome.vue'
</script>

<template>
  <div class="container col-md-14 flex-justify align-middle jumbotron vertical-center">
    <div class="row">
      <div class="col-sm p-3">
    <img alt="Brain Check" class="logo pb-4" src="@/assets/logo.png" width="125" />
    <div class="wrapper">
      <HelloWorld msg="Welcome to Brain Check." />
    </div>
    </div>
    <div class="col-sm p-3">
  <TheWelcome />
</div>
</div>

</div>
<div class="flex-justify w-100 text-center pt-5">
  <RouterLink to="/survey">
  <button type="button" class="btn btn-light justify-content-center w-75"><h3>Begin Survey  <font-awesome-icon icon="fa-solid fa-arrow-right" class="fa-xl" /></h3></button>
</RouterLink>
</div>
</template>

<style scoped>
.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
.vertical-center {
  min-height: 100%;  /* Fallback for browsers do NOT support vh unit */
  min-height: calc(100vh - 300px); /* These two lines are counted as one :-)       */

  display: flex;
  align-items: center;
}
</style>
