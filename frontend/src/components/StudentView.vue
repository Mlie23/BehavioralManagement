<template>
  <div class="bg-cornsilk h-full w-full flex-col justify-center px-2 sm:px-3">
    <div class="sm:mx-auto sm:w-full sm:max-w-6xl">
      <div class="pt-4 text-5xl font-medium">
        {{ student.first_name }} {{ student.last_name }}
      </div>
      <div class="grid grid-cols-3">
        <div class="col-span-2 grid grid-cols-2">
          <div class="pt-1 font-semibold text-xl">
            ID: {{ student.student_id }}
          </div>
          <div class="font-semibold text-xl">Grade: {{ student.grade }}</div>
          <div class="font-semibold text-xl">Gender: {{ student.gender }}</div>
          <div class="font-semibold text-xl">
            Date of Birth: {{ trim_dob(student.date_of_birth) }}
          </div>
        </div>
        <button
          @click="editStudentModal = true"
          class="font-semibold text-xl underline"
        >
          Edit
        </button>
      </div>

      <div class="pt-5">
        This page includes the list of Functional Behavioral Assessments (FBA)
        that have been completed in the past.
      </div>
      <!-- <p>
      Fill out a survey for a student
      <router-link class="hover:text-blue-600 hover:underline" to="/survey2"
        >here</router-link
      >
    </p> -->
    </div>
    <div class="flex flex-col justify-center">
      <div class="w-full flex-col justify-center py-6">
        <div class="sm:mx-auto sm:w-full sm:max-w-6xl">
          <div class="grid grid-cols-6 mb-2">
            <div class="col-span-4">
              <label
                for="default-search"
                class="mb-2 text-sm font-medium text-gray-900 sr-only"
                >Search</label
              >
              <div class="relative">
                <div
                  class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none"
                >
                  <svg
                    aria-hidden="true"
                    class="w-5 h-5 text-gray-500"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                    ></path>
                  </svg>
                </div>
                <input
                  type="search"
                  v-model="input"
                  id="default-search"
                  class="block w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-200 focus:ring-blue-500 focus:border-blue-500"
                  placeholder="Search FBAs based on FBA ID..."
                  required
                />
              </div>
            </div>
            <button
              class="ml-4 md:ml-10 col-span-2 flex flex-row bg-buff p-2 rounded-md items-center"
              @click="surveyModal = true"
            >
              <img class="relative h-8 w-8" src="../assets/plus.svg" />
              <span class="hidden md:block w-full justify-center items-center"
                >Create New FBA</span
              >
              <span
                class="block md:hidden text-sm w-full justify-center items-center"
                >New FBA</span
              >
            </button>
          </div>
          <div v-if="forms.length === 0" class="w-full mt-10">
            <div class="grid place-items-center">
              <img class="h-56 w-56" src="../assets/form.svg" alt="" />
              <p class="text-xl text-gray-400">No FBAs Created</p>
            </div>
          </div>
          <table v-else class="w-full text-sm text-left text-gray-500">
            <thead class="text-xs text-gray-700 uppercase bg-buff">
              <tr>
                <th scope="col" class="px-6 py-3">FBA ID</th>
                <th scope="col" class="px-6 py-3">TimeStamp</th>
                <th scope="col" class="pl-6 py-3">Result</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="form in filteredForms"
                :key="form.id"
                class="bg-lightbrown border-b border-black"
              >
                <th
                  scope="row"
                  class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap"
                >
                  {{ form.id }}
                </th>
                <td class="px-6 py-4">{{ trimDate(form.date) }}</td>
                <td class="px-6 py-4">
                  <button class="hover:underline" @click="viewForm(form.id)">
                    View
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
  <SurveyView v-if="surveyModal" :open="surveyModal" :student_id="student.id" />
  <EditStudentModal
    v-if="editStudentModal"
    :open="editStudentModal"
    :student_data="student"
  />
</template>

<script setup>
import SurveyView from "../components/SurveyView.vue";
/* eslint-disable */
// Import all the api functions for now only 1 from question.js api
import EditStudentModal from "../components/EditStudentModal.vue";
import { storeToRefs } from "pinia";
import { studentInfoStore } from "../store/student.js";
import { router } from "../main.js";
import * as studentApi from "../../api/student.js";
import { ref, computed } from "vue";
import { onBeforeMount } from "vue";
import moment from "moment";
import axios from "axios";
import { apiPath } from "@/constant/apiPath.js";
import { modalToggleStore } from "../store/modaltoggle.js";
const { editStudentModal, surveyModal } = storeToRefs(modalToggleStore());
const { student, formId } = storeToRefs(studentInfoStore());
const forms = ref([]);
onBeforeMount(async () => {
  forms.value = await axios
    .get(`${apiPath()}/api/prism/get_student_forms/${student?.value?.id}`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("AccessToken")}`,
      },
    })
    .then((res) => res.data)
    .catch((error) => error);
});
const input = ref("");

const trim_dob = (date) => {
  let data = moment(date).format("DD MMMM YYYY");
  if (data === "Invalid date") {
    return "NaN";
  } else {
    return data;
  }
};
const trimDate = (date) => {
  return moment(date).format("MM/DD/YYYY");
};

const viewForm = async (id) => {
  formId.value = id;
  router.push("/result");
};
// forms.value = [
//   { id: "23ab12312", timestamp: "3/3/2023" },
//   { id: "33a122312", timestamp: "3/10/2023" },
//   { id: "23aa2321e", timestamp: "3/17/2023" },
// ];

const filteredForms = computed(() => {
  const data = Object.values(forms.value).filter((form) =>
    form?.id.toString().toLowerCase().includes(input.value.toLowerCase())
  );
  return data;
});
</script>
