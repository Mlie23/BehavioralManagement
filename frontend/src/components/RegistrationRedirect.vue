<template>
  <div class="bg-cornsilk flex min-h-full flex-col justify-center py-12">
    <div class="sm:mx-auto sm:w-full sm:max-w-4xl flex flex-col items-center">
      <h3 class="text-red text-3xl md:text-5xl mb-2 text-blue-400 text-center">
        An email from
        <h3 class="text-red-500">prism.mosaic.cooperative@gmail.com</h3>
        has been sent to your email address!
      </h3>

      <h3 class="text-center">Please check your inbox and spam</h3>
      <button
        @click="router.push('/login')"
        class="inline-block mt-3 px-8 py-3 bg-blue text-white hover:shadow-lg active:bg-blue-800 active:shadow-lg"
      >
        Login
      </button>
    </div>
  </div>
</template>

<script setup>
/* eslint-disable */
import { router } from "../main.js";
</script>
