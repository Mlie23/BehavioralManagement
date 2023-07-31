import { defineStore } from "pinia";
import { ref } from "vue";
export const studentInfoStore = defineStore("studentinfo", {
  state: () => {
    const student = ref({});
    const formId = ref();
    return { student, formId };
  },
  persist: { storage: sessionStorage },
});

export default { studentInfoStore };
