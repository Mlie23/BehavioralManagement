<template>
  <div role="alert">
    <div class="bg-red-500 text-white font-bold rounded-t px-4 py-2 relative">
      <strong v-if="!props.headers" class="font-semibold text-xl">Error</strong>
      <strong v-else class="font-semibold text-xl">{{ props.headers }}</strong>
      <!-- <button class="absolute top-0 right-0 px-4 py-3" @click="emit('close')">
        <svg
          class="fill-current h-6 w-6 text-white"
          role="button"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 20 20"
        >
          <title>Close</title>
          <path
            d="M14.348 14.849a1.2 1.2 0 0 1-1.697 0L10 11.819l-2.651 3.029a1.2 1.2 0 1 1-1.697-1.697l2.758-3.15-2.759-3.152a1.2 1.2 0 1 1 1.697-1.697L10 8.183l2.651-3.031a1.2 1.2 0 1 1 1.697 1.697l-2.758 3.152 2.758 3.15a1.2 1.2 0 0 1 0 1.698z"
          />
        </svg>
      </button> -->
    </div>

    <div class="bg-red-100">
      <div class="grid grid-cols-2">
        <div
          v-for="error in props.loginerror"
          :key="error.message"
          class="rounded-b bg-red-100 px-4 py-1 text-red-700"
          :class="{ 'col-span-2': props.fullgrid }"
        >
          <p>{{ error }}</p>
        </div>
        <div
          v-for="error in props.errors"
          :key="error.message"
          class="rounded-b bg-red-100 px-4 py-1 text-red-700"
        >
          <p>{{ error }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
/*eslint-disable*/

const props = defineProps({
  headers: { type: String, required: false },
  fullgrid: { type: Boolean, required: false },
  errors: { type: Object, required: true },
  loginerror: { type: Object, required: false },
});
const emit = defineEmits("close");
</script>
