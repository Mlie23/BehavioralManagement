import { defineStore } from "pinia";
import { ref } from "vue";
const modalToggleStore = defineStore("modaltoggle", {
  state: () => {
    const editStudentModal = ref(false);
    const passwordModal = ref(false);
    const errorModal = ref(false);
    const resendVerificationModal = ref(false);
    const resetPasswordModal = ref(false);
    const surveyModal = ref(false);
    const surveyResultModal = ref(false);
    const accountModal = ref(false);
    const createStudentModal = ref(false);
    const editAccountModal = ref(false);
    const changePassword = ref(false);
    return {
      createStudentModal,
      editStudentModal,
      passwordModal,
      errorModal,
      resendVerificationModal,
      resetPasswordModal,
      surveyModal,
      surveyResultModal,
      accountModal,
      editAccountModal,
      changePassword,
    };
  },
  persist: { storage: sessionStorage },
});

export { modalToggleStore };
