import { defineStore } from "pinia";
import { ref } from "vue";
export const tokenStore = defineStore("tokenStore", {
  state: () => {
    const token = ref({});
    return { token };
  },
  persist: { storage: localStorage },
});

export default { tokenStore };
