<template>
  <TransitionRoot :show="props.open">
    <Dialog @close="passwordModal = false" class="relative">
      <DialogPanel>
        <!--<DialogTitle>Update account</DialogTitle>-->
        <div
          class="fixed h-full inset-0 z-10 overflow-y-auto bg-gray-500/[0.95] flex-col justify-center"
        >
          <div class="sm:w-full relative sm:mx-auto sm:max-w-6xl px-12 h-full">
            <DialogPanel class="relative h-full">
              <div class="flex flex-col justify-center h-full">
                <div class="sm:mx-auto sm:w-full sm:max-w-2xl">
                  <div
                    class="bg-white rounded shadow-2xl bg-gray-100 text-black m-5 sm:m-0 border-2 border-gray-400"
                  >
                    <div
                      class="flex flex-col-2 justify-between mb-8 border border-gray-200 p-5"
                    >
                      <h1 class="text-3xl">Edit Profile</h1>

                      <button @click="passwordModal = false">
                        <img
                          class="h-8 w-8"
                          src="../assets/x_button.jpg"
                          alt=""
                        />
                      </button>
                    </div>

                    <form @submit="onSubmit">
                      <div class="px-6 pb-4">
                        <ErrorModalView
                          class="mb-5"
                          :loginerror="{ invalid: submitErrors }"
                          :fullgrid="true"
                          :errors="errors"
                          v-if="
                            errors.old_password ||
                            errors.new_password ||
                            errors.new_password2 ||
                            submitErrors != ''
                          "
                        ></ErrorModalView>

                        <p>Old Password</p>

                        <div class="w-full">
                          <div class="relative">
                            <svg
                              class="absolute top-2 right-2 w-6 h-6"
                              @click="showOldPassword = true"
                              v-if="!showOldPassword"
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
                              @click="showOldPassword = false"
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
                              v-if="!showOldPassword"
                              id="Old_password"
                              v-model="old_password"
                              type="password"
                              class="block w-full rounded-lg border-2 border-box mb-2 mr-2 pl-2 py-2"
                              placeholder="Old Password"
                              :class="{
                                'border-red-500 placeholder-red-500':
                                  errors.old_password,
                              }"
                            />
                            <input
                              v-else
                              id="Old_password"
                              v-model="old_password"
                              type="text"
                              class="block w-full rounded-lg border-2 border-box mb-2 mr-2 pl-2 py-2"
                              placeholder="Old Password"
                              :class="{
                                'border-red-500 placeholder-red-500':
                                  errors.old_password,
                              }"
                            />
                          </div>
                          <p>New Password</p>

                          <div class="relative">
                            <svg
                              class="absolute top-2 right-2 w-6 h-6"
                              @click="showNewPassword1 = true"
                              v-if="!showNewPassword1"
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
                              @click="showNewPassword1 = false"
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
                              v-if="!showNewPassword1"
                              id="Last_name"
                              type="password"
                              v-model="new_password"
                              class="block w-full rounded-lg border-2 border-box mb-2 mr-2 pl-2 py-2"
                              placeholder="New Password"
                              :class="{
                                'border-red-500 placeholder-red-500':
                                  errors.new_password,
                              }"
                            />
                            <input
                              v-else
                              id="Last_name"
                              type="text"
                              v-model="new_password"
                              class="block w-full rounded-lg border-2 border-box mb-2 mr-2 pl-2 py-2"
                              placeholder="New Password"
                              :class="{
                                'border-red-500 placeholder-red-500':
                                  errors.new_password,
                              }"
                            />
                          </div>
                        </div>

                        <p>Confirm New Password</p>
                        <div class="relative">
                          <svg
                            class="absolute top-2 right-2 w-6 h-6"
                            @click="showNewPassword2 = true"
                            v-if="!showNewPassword2"
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
                            @click="showNewPassword2 = false"
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
                            v-if="!showNewPassword2"
                            id="new_password2"
                            type="password"
                            v-model="new_password2"
                            class="block w-full rounded-lg border-2 border-box mb-10 pl-2 py-2"
                            placeholder="Confirm New Password"
                            :class="{
                              'border-red-500 placeholder-red-500':
                                errors.new_password2,
                            }"
                          />
                          <input
                            v-else
                            id="new_password2"
                            type="text"
                            v-model="new_password2"
                            class="block w-full rounded-lg border-2 border-box mb-10 pl-2 py-2"
                            placeholder="Confirm New Password"
                            :class="{
                              'border-red-500 placeholder-red-500':
                                errors.new_password2,
                            }"
                          />
                        </div>

                        <button
                          type="submit"
                          class="inline-block mt-3 px-6 py-2.5 bg-gray-500 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg active:bg-blue-800 active:shadow-lg"
                        >
                          Update
                        </button>
                      </div>
                    </form>
                  </div>
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
import {
  TransitionRoot,
  Dialog,
  DialogPanel,
  //DialogTitle,
} from "@headlessui/vue";
import axios from "axios";
//import { ref } from "vue";
import * as yup from "yup";
import { useForm, useField } from "vee-validate";
import * as teacherApi from "../../api/teacher.js";
import { router } from "../main.js";
import { ref } from "vue";
import ErrorModalView from "@/components/ErrorModalView.vue";
import { storeToRefs } from "pinia";
import { onBeforeMount } from "vue";
import { teacherInfoStore } from "../store/teacherinfo.js";
import { apiPath } from "@/constant/apiPath";
import { modalToggleStore } from "../store/modaltoggle.js";
const { passwordModal } = storeToRefs(modalToggleStore());
const { teacherInfo } = storeToRefs(teacherInfoStore());
const showOldPassword = ref(false);
const showNewPassword1 = ref(false);
const showNewPassword2 = ref(false);
const UserSchema = yup.object().shape({
  old_password: yup
    .string()
    .required("Old Password is required")
    .max(50, "Maximum character is 50"),
  new_password: yup
    .string()
    .required("New Password is required")
    .max(50, "Maximum character is 50"),
  new_password2: yup
    .string()
    .required("New Password Confirmation is required")
    .max(50, "Maximum character is 50")
    .oneOf([yup.ref("new_password")], "Password must match"),
});

const { errors, handleSubmit } = useForm({
  validationSchema: UserSchema,
});

const props = defineProps({
  open: { type: Boolean, required: true },
});
const emit = defineEmits("close");

const errorState = ref(false);
const submitErrors = ref("");

const { value: old_password } = useField("old_password");
const { value: new_password } = useField("new_password");
const { value: new_password2 } = useField("new_password2");

const onSubmit = handleSubmit(async (values) => {
  await updatePassword(values);
});

const updatePassword = async (values) => {
  const data = await axios
    .put(`${apiPath()}/api/prism/change-password`, values, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("AccessToken")}`,
      },
    })
    .then(function (response) {
      return response.data;
    })
    .catch(function (error) {
      return error;
    });
  if (data?.code !== 200) {
    errorState.value = true;
    submitErrors.value = data.response.data[0];
  } else {
    //   errorState.value = false;
    //   teacherInfo.value = values;
    passwordModal.value = false;
    // location.reload();
    // router.push("/profile");
  }
};
</script>
