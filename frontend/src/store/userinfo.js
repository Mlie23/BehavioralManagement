import { defineStore } from "pinia";
import { ref } from "vue";
export const userInfoStore = defineStore("userinfo", {
  state: () => {
    const { userinfo } = ref({});
    return { userinfo };
  },
  persist: { storage: localStorage },
});

export default { userInfoStore };
