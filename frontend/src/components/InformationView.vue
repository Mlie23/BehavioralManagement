<template>
  <div class="h-full">
    <div class="ml-4 text-gray-700">
      <h1 class="text-2xl">My Profile</h1>
      <p>Name: {{ name }}</p>
      <p>Username: {{ username }}</p>
      <p>Email: {{ email }}</p>
      <p>School: {{ school }}</p>
    </div>
    <button
      class="text-gray-800 bg-sienna hover:bg-gray-400 hover:text-white px-3 py-2 rounded-md text-sm font-medium"
      @click="increment()"
    >
      Increment me {{ number }}
    </button>
    <button
      class="text-gray-800 bg-sienna hover:bg-gray-400 hover:text-white px-3 py-2 rounded-md text-sm font-medium"
      @click="incrementDummy()"
    >
      Increment me {{ dummy }}
    </button>
  </div>
</template>

<script setup>
/* eslint-disable */
import { ref } from "vue";
import { storeToRefs } from "pinia";
import { userInfoStore } from "../store/userinfo.js";
const { userinfo } = storeToRefs(userInfoStore());
const name = "John Doe";
const email = "smnek@gmail.com";
const school = "SMNEK Elementary School";
const username = ref();
username.value = "smnek";
const number = ref(0);
const increment = () => {
  number.value += 1;
};

const dummy = 0;
const incrementDummy = () => {
  dummy += 1;
};
</script>
