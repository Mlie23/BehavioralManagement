<template>
  <div class="bg-cornsilk flex h-full w-full flex-col justify-center">
    <div class="sm:mx-auto sm:w-full sm:max-w-4xl px-3 pt-5">
      <div class="grid grid-cols-2 justify-center gap-8 h-full">
        <div
          class="bg-lightbrown flex flex-col justify-center items-center rounded-lg border-2 border-box"
        >
          <!-- <div class="relative top-0 rounded-lg w-full py-5 bg-buff"></div> -->
          <div class="flex full border-2">
            <img
              class="h-56 w-56 rounded-full"
              src="../assets/profile.svg"
              alt=""
            />
          </div>

          <div class="text-2xl font-medium mt-4">
            {{ teacherInfo.first_name }} {{ teacherInfo.last_name }}
          </div>
        </div>

        <div
          class="bg-lightbrown flex flex-col items-center w-full rounded-lg border-2 border-box"
        >
          <div class="rounded-lg w-full py-5 bg-buff"></div>
          <ErrorModalView
            class="mb-5"
            :headers="'Warning!'"
            :fullgrid="true"
            :loginerror="{ teacher: 'Please fill your profile information' }"
            v-if="teacherInfo === 404"
          ></ErrorModalView>
          <div class="text-2xl font-medium m-4">Profile Information</div>
          <div class="">
            Name: {{ teacherInfo.first_name }} {{ teacherInfo.last_name }}
          </div>
          <div class="">School: {{ teacherInfo.school }}</div>
          <button
            class="inline-block mt-3 px-8 py-3 bg-cornsilk font-medium text-lg leading-tight rounded shadow-md hover:bg-brown hover:shadow-lg active:bg-blue-800 active:shadow-lg"
            @click="accountModal = true"
          >
            Edit Profile
          </button>
          <div class="text-2xl font-medium m-4">Sign in & security</div>
          <div class="">Email: {{ userinfo.user.email }}</div>
          <div class="">Username: {{ userinfo.user.username }}</div>
          <div class="">Password: **********</div>
          <button
            class="inline-block mt-3 px-8 py-3 bg-cornsilk font-medium text-lg leading-tight rounded shadow-md hover:bg-brown hover:shadow-lg active:bg-blue-800 active:shadow-lg"
            @click="passwordModal = true"
          >
            Change Password
          </button>
        </div>
      </div>
    </div>
  </div>
  <AccountModal
    v-if="accountModal"
    :open="accountModal"
    @close="accountModal = false"
  />
  <PasswordView
    v-if="passwordModal"
    :open="passwordModal"
    @close="passwordModal = false"
  />
</template>

<script setup>
/*eslint-disable*/
import ErrorModalView from "./ErrorModalView.vue";
import { ref } from "vue";
import AccountModal from "../components/AccountModal.vue";
import PasswordView from "../components/PasswordModal.vue";
import { onBeforeMount } from "vue";
import { storeToRefs } from "pinia";
import { userInfoStore } from "../store/userinfo.js";
import { teacherInfoStore } from "../store/teacherinfo.js";
import axios from "axios";
import { apiPath } from "@/constant/apiPath";
import { modalToggleStore } from "../store/modaltoggle.js";
const { passwordModal, accountModal } = storeToRefs(modalToggleStore());

const { teacherInfo } = storeToRefs(teacherInfoStore());
const { userinfo } = storeToRefs(userInfoStore());

//import { router } from "../main.js";
const warning = ref(false);
onBeforeMount(async () => {
  teacherInfo.value = await axios
    .get(`${apiPath()}/api/prism/get_teacher`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("AccessToken")}`,
      },
    })
    .then((res) => {
      return res.data;
    })
    .catch((error) => {
      return error.response.status;
    });
  if (teacherInfo.value === 404) {
    warning.value = true;
  }
});
</script>
