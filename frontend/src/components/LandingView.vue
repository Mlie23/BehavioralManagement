<template>
  <!-- vue-cli-documentation: "https://cli.vuejs.org" -->
  <div class="bg-cornsilk h-full">
    <div class="bg-cornsilk max-w-5xl mx-auto h-full px-6">
      <div class="grid grid-cols-2 place-items-center h-full">
        <div class="col-span-2 sm:col-span-1 text-gray-700">
          <div class="font-semibold text-6xl">
            <div class="bg-cornsilk sm:hidden flex flex-col items-center">
              <h1>PRISM</h1>
            </div>
            <div class="hidden sm:block">
              <h1>PRISM</h1>
            </div>
            <hr class="h-px my-1 bg-red-300 border-0" />
          </div>
          <div class="sm:px-0 px-5">
            <h3 class="text-xl font-medium">Founders Vision</h3>
            <p>{{ founderVision }}</p>
          </div>
          <div class="mt-8 w-full flex flex-col items-center">
            <button
              @click="router.push('/dashboard')"
              class="bg-blue py-4 px-14 rounded-3xl font-bold text-xl text-cornsilk"
            >
              Login
            </button>
          </div>
        </div>
        <div class="hidden sm:block col-span-1 justify-center items-center">
          <img src="../assets/prism.svg" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
/* eslint-disable */
import { ref } from "vue";
import { router } from "../main.js";
const founderVision = ref();
founderVision.value =
  "Welcome to the self-guided behavior support planning tool. You will be asked a series of questions and then be provided with a customized set of strategies for supporting the behavioral needs of one of your students.";
</script>
