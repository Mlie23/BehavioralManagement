<template>
  <!-- <img alt="Vue logo" src="@/assets/logo.png"> -->
  <div class="flex flex-col h-screen">
    <header>
      <nav-bar v-if="isAuthenticated" />
    </header>
    <main class="flex-grow">
      <router-view />
    </main>
  </div>
</template>

<script setup>
/* eslint-disable */

import { storeToRefs } from "pinia";
import HelloWorld from "./components/LandingView.vue";
import SurveyView from "./components/SurveyView.vue";
import NavBar from "./components/NavBar.vue";
import { userStateStore } from ".//store/userstate.js";
const { isAuthenticated } = storeToRefs(userStateStore());
</script>
