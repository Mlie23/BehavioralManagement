<template>
  <div class="bg-cornsilk flex min-h-full flex-col justify-center py-12">
    <div class="sm:mx-auto sm:w-full sm:max-w-2xl flex flex-col items-center">
      <h1 class="text-7xl text-red-400">404</h1>
      <h3 class="text-red text-5xl mb-2 text-red-400">
        Error, Page not Found!
      </h3>
      <h3 class="text-center">
        The page you are looking for might have been removed, had its name
        changed or is temporarily unavailable.
      </h3>
      <button
        @click="router.back()"
        class="inline-block mt-3 px-8 py-3 bg-blue text-white hover:shadow-lg active:bg-blue-800 active:shadow-lg"
      >
        Go Back
      </button>
    </div>
  </div>
</template>

<script setup>
/* eslint-disable */
import { router } from "../main.js";
</script>
