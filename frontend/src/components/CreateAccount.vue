<template>
  <div class="bg-cornsilk flex flex-col justify-center h-full">
    <div class="sm:mx-auto sm:w-full sm:max-w-2xl">
      <form autocomplete="off" @submit="onSubmit">
        <div
          class="bg-lightbrown rounded shadow-2xl text-black m-5 sm:m-0 border-2 border-gray-400"
        >
          <div class="px-6 py-6">
            <h1 class="text-3xl mb-8 text-center">Create a New Account</h1>
            <div v-if="errorState">
              <div class="bg-red-500 text-white font-bold rounded-t py-1"></div>
              <div
                class="border border-t-0 border-red-400 rounded-b bg-red-100 px-4 py-3 text-red-700"
              >
                <p class="font-bold">Invalid Credentials</p>

                <div v-for="key in Object.keys(submitErrors)" :key="key.id">
                  {{ submitErrors[key][0] }}
                </div>
              </div>
            </div>
            <ErrorModalView
              class="mb-5"
              :errors="errors"
              v-if="
                errors.username ||
                errors.password1 ||
                errors.password2 ||
                errors.email
              "
            ></ErrorModalView>
            <p>Create a username:</p>
            <input
              id="Username"
              autocomplete="off"
              v-model="username"
              class="block w-full rounded-lg border-2 border-box mb-2 pl-2 py-2"
              placeholder="Username"
              :class="{ 'border-red-500': errors.username }"
            />

            <p>Enter your email:</p>
            <input
              id="Email"
              v-model="email"
              class="block w-full rounded-lg border-2 border-box mb-2 pl-2 py-2"
              placeholder="Email"
              :class="{ 'border-red-500': errors.email }"
            />

            <!-- why "email rules" -->
            <p>Create a password:</p>
            <div class="relative">
              <svg
                class="absolute top-2 right-2 w-6 h-6"
                @click="showPassword1 = true"
                v-if="!showPassword1"
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
                @click="showPassword1 = false"
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
              </svg>
              <input
                v-if="showPassword1"
                autocomplete="off"
                type="text"
                id="password1"
                v-model="password1"
                name="emailRules"
                placeholder="Password"
                class="select-none block w-full rounded-lg border-2 border-box pl-2 py-2"
                :class="{ 'border-red-500': errors.password1 }"
              />
              <input
                v-else
                autocomplete="off"
                type="password"
                id="password1"
                v-model="password1"
                name="emailRules"
                placeholder="Password"
                class="select-none block w-full rounded-lg border-2 border-box pl-2 py-2"
                :class="{ 'border-red-500': errors.password1 }"
              />
            </div>
            <p>Confirm Password:</p>
            <div class="relative">
              <svg
                class="absolute top-2 right-2 w-6 h-6"
                @click="showPassword2 = true"
                v-if="!showPassword2"
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
                @click="showPassword2 = false"
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
              </svg>
              <input
                v-if="showPassword2"
                autocomplete="new-password"
                type="text"
                id="password2"
                v-model="password2"
                name="emailRules"
                placeholder="Password"
                class="select-none block w-full rounded-lg border-2 border-box pl-2 py-2"
                :class="{ 'border-red-500': errors.password2 }"
              />
              <input
                v-else
                autocomplete="new-password"
                type="password"
                id="password2"
                v-model="password2"
                name="emailRules"
                placeholder="Password"
                class="select-none block w-full rounded-lg border-2 border-box pl-2 py-2"
                :class="{ 'border-red-500': errors.password2 }"
              />
            </div>
            <div class="flex flex-col items-center">
              <button
                type="submit"
                id="Sign in"
                class="inline-block mt-3 px-8 py-3 bg-white font-medium text-xs leading-tight rounded shadow-md hover:bg-blue-700 hover:shadow-lg active:bg-blue-800 active:shadow-lg"
              >
                Create Account
              </button>
            </div>
            <!-- <button
              type="submit"
              id="submit"
              class="inline-block mt-3 px-6 py-2.5 bg-gray-500 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg active:bg-blue-800 active:shadow-lg"
              @click="onSubmit"
            >
              Create Account
            </button> -->
          </div>
        </div>
      </form>
      <p class="text-center">
        Already have an account?
        <router-link class="hover:text-indigo-500 hover:underline" to="/login"
          >Log in here.</router-link
        >
      </p>
    </div>
  </div>
</template>

<script setup>
/*eslint-disable*/

import { useForm, useField } from "vee-validate";
import * as registrationApi from "../../api/registration.js";
import { router } from "../main.js";
import ErrorModalView from "./ErrorModalView.vue";
// Yup behaves like regex (find things in the string)
// It is pretty neat and helpful to use yup
// It can identifies email, requirement, and you can create your own rules (using regex and dependence of other fields)
// Any question, send me a text!
import * as yup from "yup";
import { ref } from "vue";
// Create a schema that will handle the form and its rule

const RegisterSchema = yup.object().shape({
  username: yup.string().required("Username is required"),
  email: yup
    .string()
    .required("Email is required")
    .email("Invalid email address"),
  password1: yup
    .string()
    .required("Password is required")
    .min(8, "Password is too short"),
  password2: yup
    .string()
    .required("Password Confirmation is required")
    .oneOf([yup.ref("password1")], "Passwords must match"),
});

// Inject errors and submit dependency to our form
const { errors, handleSubmit } = useForm({
  validationSchema: RegisterSchema,
});
const { value: username } = useField("username");
const { value: email } = useField("email");
const { value: password1 } = useField("password1");
const { value: password2 } = useField("password2");

const errorState = ref(false);
const submitErrors = ref();
const showPassword1 = ref(false);
const showPassword2 = ref(false);
//const errorSubmit = ref();
// If requirements are passed, this button will be called
// Future purpose: Store user info and local storage
// Route user to available webpages based on their roles

const onSubmit = handleSubmit(async (values) => {
  let result = await registration(values);
  // await router.push to somewhere
});

const registration = async (values) => {
  const data = await registrationApi.register(values);
  if (data?.response?.request?.status === 400) {
    errorState.value = true;
    submitErrors.value = data.response.data;

    //} else if (data.response.request.status === 500) {
    //  errorState.value = true;
  } else {
    errorState.value = false;
    router.push("/registrationredirect");
  }
};
</script>
