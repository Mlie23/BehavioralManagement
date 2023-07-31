<template>
  <TransitionRoot :show="props.open">
    <Dialog @close="resendVerificationModal = false" class="fixed">
      <DialogPanel>
        <div
          class="fixed h-full inset-0 z-10 flex w-full items-center justify-center py-12 bg-gray-500/[0.8]"
        >
          <!-- <div class="relative"> -->
          <div class="w-full relative sm:mx-auto sm:max-w-2xl">
            <DialogPanel class="relative">
              <div
                class="rounded shadow-2xl bg-lightbrown text-black m-5 sm:m-0 border-2 border-gray-400"
              >
                <button
                  type="close"
                  @click="resendVerificationModal = false"
                  class="absolute right-0 w-10 h-10"
                >
                  <img src="../assets/close.png" />
                </button>
                <div class="px-6 py-6">
                  <form @submit="onSubmit">
                    <!--    <form>-->

                    <h1 class="text-3xl mb-8 text-center">
                      Email Verification
                    </h1>
                    <ErrorModalView
                      v-if="errors.email || errorState"
                      :fullgrid="true"
                      :errors="errors"
                      :loginerror="{ invalid: invalidMessage }"
                    />
                    <!-- <label> Email </label> -->
                    <!-- If email does not match yup requirement, error state will appear-->
                    <!-- {{ student_data }} -->

                    <!-- If username does not match yup requirement, error state will appear -->
                    <p>Email</p>
                    <input
                      type="email"
                      id="email"
                      v-model="email"
                      name="idRules"
                      placeholder="Email"
                      class="block w-full rounded-lg border-2 border-box pl-2 py-2"
                      :class="{ 'border border-red-500': errors.email }"
                    />
                    <div class="w-full flex justify-center items-center">
                      <button
                        type="submit"
                        class="block grid place-items-center justify-center inline-block mt-3 px-6 py-2.5 text-black font-medium text-lg bg-cornsilk hover:underline leading-tight rounded shadow-md hover:bg-blue-700 hover:shadow-lg active:bg-blue-800 active:shadow-lg"
                      >
                        Resend Verification
                      </button>
                    </div>
                  </form>
                </div>
              </div>
            </DialogPanel>
          </div>
        </div>
      </DialogPanel>
    </Dialog>
  </TransitionRoot>
</template>

<script setup>
/* eslint-disable */
import ErrorModalView from "../components/ErrorModalView.vue";
import {
  TransitionRoot,
  Dialog,
  DialogPanel,
  DialogTitle,
} from "@headlessui/vue";
import { useForm, useField } from "vee-validate";
import { storeToRefs } from "pinia";
// import { userStateStore } from "../store/userstate.js";
// import { userInfoStore } from "../store/userinfo.js";
import { router } from "../main.js";
import "@vuepic/vue-datepicker/dist/main.css";
import * as yup from "yup";
import { ref } from "vue";
import moment from "moment";
import VueTailwindDatepicker from "vue-tailwind-datepicker";
import { studentInfoStore } from "../store/student.js";
import axios from "axios";
import { apiPath } from "@/constant/apiPath.js";
import { modalToggleStore } from "../store/modaltoggle.js";
const { resendVerificationModal } = storeToRefs(modalToggleStore());
const { student } = storeToRefs(studentInfoStore());
const invalidMessage = ref("");
const props = defineProps({
  open: { type: Boolean, required: true },
});
const emit = defineEmits("close");
const RegisterSchema = yup.object().shape({
  email: yup
    .string()
    .required("Email is required")
    .email("Invalid email address"),
});
// Inject errors and submit dependency to our form
const { errors, handleSubmit } = useForm({
  validationSchema: RegisterSchema,
});

const { value: email } = useField("email");
// const {value:name} = useField('name');

const errorState = ref(false);
// If requirements are passed, this button will be called
// Future purpose: Store user info and local storage
// Route user to available webpages based on their roles

const onSubmit = handleSubmit(async (values) => {
  const data = await axios
    .post(`${apiPath()}/api/prism/resend_verification`, values, {})
    .then((res) => {
      return res.data;
    })
    .catch((err) => {
      return err;
    });
  if (data?.response?.status === 403) {
    invalidMessage.value = "Email is verified, please proceed to login";
    errorState.value = true;
  } else {
    resendVerificationModal.value = false;
    await router.push("/registrationredirect");
  }
});
</script>
