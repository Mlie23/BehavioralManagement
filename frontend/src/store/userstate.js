import { defineStore } from "pinia";
import { ref } from "vue";
const userStateStore = defineStore("userstate", {
  state: () => {
    const isAuthenticated = ref(false);
    return { isAuthenticated };
  },
  persist: { storage: sessionStorage },
});

export { userStateStore };
