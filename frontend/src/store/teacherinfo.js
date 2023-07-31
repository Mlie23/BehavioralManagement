import { defineStore } from "pinia";
import { ref } from "vue";
export const teacherInfoStore = defineStore("teacherInfo", {
  state: () => {
    const { teacherInfo } = ref({});
    return { teacherInfo };
  },
  persist: { storage: localStorage },
});

export default { teacherInfoStore };
