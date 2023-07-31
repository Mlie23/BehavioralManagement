<template>
  <div class="bg-cornsilk flex min-h-full flex-col justify-center py-12">
    <div class="sm:mx-auto sm:w-full sm:max-w-2xl">
      <form @submit="onSubmit">
        <div
          class="h-full bg-lightbrown rounded shadow-2xl bg-gray-100 text-black m-5 sm:m-0 border-2 border-gray-400"
        >
          <div class="px-6 py-3">
            <h1 class="mb-5 text-3xl text-center">Login</h1>
            <ErrorModalView
              class="mb-5"
              :loginerror="{ invalid: invalidMessage }"
              :fullgrid="true"
              :errors="errors"
              v-if="errorState || errors.username || errors.password"
            ></ErrorModalView>
            <p>Username / Email</p>
            <input
              id="Username"
              v-model="username"
              class="block w-full border-2 rounded-lg border-box mb-4 p-1"
              placeholder="Username or Email..."
              :class="{ 'border-red-500': errors.username }"
            />
            <!-- <label> Email </label> -->
            <!-- If email does not match yup requirement, error state will appear -->
            <!-- <span
              v-if="errors.email"
              class="flex items-center px-2 bg-buff border-1 border-buff text-brown"
            >
              {{ errors.email }}
            </span> -->
            <!-- <input
              id="Email"
              v-model="email"
              class="block w-full border-2 border-box mb-4 p-1"
              placeholder="Email"
              :class="{ 'border-buff': errors.email }"
            /> -->
            <!-- <label>Password</label> -->
            <!-- If password does not match yup requirement, error state will appear -->
            <p>Password</p>
            <div class="relative">
              <!-- <svg
                class="absolute top-2 right-2 w-6 h-6"
                @click="showPassword = true"
                v-if="!showPassword"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z"
                />
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                />
              </svg>
              <svg
                @click="showPassword = false"
                v-else
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="absolute top-2 right-2 w-6 h-6"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M3.98 8.223A10.477 10.477 0 001.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.45 10.45 0 0112 4.5c4.756 0 8.773 3.162 10.065 7.498a10.523 10.523 0 01-4.293 5.774M6.228 6.228L3 3m3.228 3.228l3.65 3.65m7.894 7.894L21 21m-3.228-3.228l-3.65-3.65m0 0a3 3 0 10-4.243-4.243m4.242 4.242L9.88 9.88"
                />
              </svg> -->
              <!-- v-if="!showPassword" -->
              <input

                type="password"
                id="password"
                v-model="password"
                name="emailRules"
                placeholder="Password"
                class="block w-full border-2 rounded-lg border-box p-1"
                :class="{ 'border-red-500': errors.password }"
              />
              <!-- <input
                v-else
                type="text"
                id="password"
                v-model="password"
                name="emailRules"
                placeholder="Password"
                class="block w-full border-2 rounded-lg border-box p-1"
                :class="{ 'border-red-500': errors.password }"
              /> -->
            </div>
            <div class="relative">
              <button
                @click="resetPasswordModal = true"
                type="button"
                class="text-sm absolute right-2 pb-2 hover:text-indigo-500 hover:underline hover:font-semibold"
              >
                Forgot Password?
              </button>
            </div>
            <!-- <input v-if="showPassword" type="text" class="input" v-model="password" />
           <input v-else type="password" class="input" v-model="password"> -->
            <div class="flex flex-col items-center">
              <button
                type="submit"
                id="Sign in"
                class="inline-block mt-3 px-8 py-3 bg-white font-medium text-xs leading-tight rounded shadow-md hover:bg-blue-700 hover:shadow-lg active:bg-blue-800 active:shadow-lg"
              >
                Sign In
              </button>
            </div>
          </div>
        </div>
      </form>
      <div class="flow-root">
        <p class="float-left">
          <router-link
            class="pl-6 hover:text-indigo-500 hover:underline hover:font-semibold"
            to="/createaccount"
            >Don't have an account?</router-link
          >
        </p>

        <p class="float-right">
          <button
            @click="resendVerificationModal = true"
            class="pr-6 hover:text-indigo-500 hover:underline hover:font-semibold"
            to="/createaccount"
          >
            Verification issues?
          </button>
        </p>
      </div>
    </div>
  </div>
  <ResendVerification
    v-if="resendVerificationModal"
    :open="resendVerificationModal"
    @close="resendVerificationModal = false"
  />
  <ResetPasswordModal
    v-if="resetPasswordModal"
    :open="resetPasswordModal"
    @close="resetPasswordModal = false"
  />
</template>

<script setup>
/* eslint-disable */
// See vee-validate documentation for further explanation
import { useForm, useField } from "vee-validate";
import { storeToRefs } from "pinia";
import { userStateStore } from "../store/userstate.js";
import { userInfoStore } from "../store/userinfo.js";
import * as registrationApi from "../../api/registration.js";
import * as teacherApi from "../../api/teacher.js";
import { router } from "../main.js";
import * as yup from "yup";
import { ref } from "vue";
import ResendVerification from "@/components/ResendVerificationModal.vue";
import ErrorModalView from "@/components/ErrorModalView.vue";
import ResetPasswordModal from "@/components/ResetPasswordModal.vue";
import { modalToggleStore } from "../store/modaltoggle.js";
const { resendVerificationModal, resetPasswordModal } = storeToRefs(
  modalToggleStore()
);
const { userinfo } = storeToRefs(userInfoStore());
const invalidMessage = ref("");
const showPassword = ref(false);
const resetPassword = ref(false);
// Yup behaves like regex (find things in the string)
// It is pretty neat and helpful to use yup
// It can identifies email, requirement, and you can create your own rules (using regex and dependence of other fields)
// Any question, send me a text!
const { isAuthenticated } = storeToRefs(userStateStore());
const { teacher } = storeToRefs(userInfoStore());
//const { token } = storeToRefs(tokenStore());
const verificationModal = ref(false);
// Create a schema that will handle the form and its rule
const loginSchema = yup.object().shape({
  username: yup.string().required("Username is required"),
  // email: yup
  //   .string()
  //   .required("Email is required")
  //   .email("Invalid email address"),
  password: yup
    .string()
    .required("Password is required")
    .min(8, "Password is too short"),
});

// Inject errors and submit dependency to our form
const { errors, handleSubmit } = useForm({
  validationSchema: loginSchema,
});

const { value: username } = useField("username");
// const { value: email } = useField("email");
const { value: password } = useField("password");
const errorState = ref(false);
// If requirements are passed, this button will be called
// Future purpose: Store user info and local storage
// Route user to available webpages based on their roles
const onSubmit = handleSubmit(async (values) => {
  let result = await login(values);
  return result;
  // await router.push to somewhere
});
const login = async (values) => {
  const data = await registrationApi.login(values);
  if (data?.response?.status === 400) {
    errorState.value = true;
    invalidMessage.value = data.response.data.non_field_errors[0];
    isAuthenticated.value = false;
  } else {
    localStorage.setItem("AccessToken", data?.access_token);
    localStorage.setItem("RefreshToken", data?.refresh_token);
    userinfo.value = data;
    isAuthenticated.value = true;
    await credentials();
  }
};

const credentials = async () => {
  const data = await teacherApi.getTeacherInfo();
  if (data?.response?.request?.status === 404) {
    router.push("/profile");
  } else {
    router.push("/dashboard");
  }
};
</script>
