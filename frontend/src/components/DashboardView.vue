<template>
  <div class="bg-cornsilk h-full w-full flex-col justify-center px-2 sm:px-3">
    <div class="sm:mx-auto sm:w-full sm:max-w-6xl">
      <div class="pt-4 text-6xl font-medium">
        {{ teacherInfo.first_name }} {{ teacherInfo.last_name }}'s Students
      </div>
      <div class="text-3xl font-medium pb-5">{{ teacherInfo.school }}</div>

      <!-- <p>
      Fill out a survey for a student
      <router-link class="hover:text-blue-600 hover:underline" to="/survey2"
        >here</router-link
      >
    </p> -->
    </div>
    <div class="flex flex-col justify-center">
      <div class="w-full flex-col justify-center pb-6">
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
                  placeholder="Search student based on Name or Student ID..."
                  required
                />
              </div>
            </div>
            <button
              class="ml-4 md:ml-10 col-span-2 flex flex-row bg-buff p-2 rounded-md items-center"
              @click="createStudentModal = true"
            >
              <img class="relative h-8 w-8 sm:mr-4" src="../assets/plus.svg" />
              <span class="hidden md:block w-full justify-center items-center"
                >Create New Student</span
              >
              <span
                class="block md:hidden text-sm w-full justify-center items-center"
                >New Student</span
              >
            </button>
          </div>
          <div v-if="students.length === 0" class="w-full mt-10">
            <div class="grid place-items-center">
              <img class="h-56 w-56" src="../assets/pencil.svg" alt="" />
              <p class="text-xl text-gray-400">No Student Created</p>
            </div>
          </div>
          <table v-else class="w-full text-sm text-left text-gray-500">
            <thead class="text-xs text-gray-700 uppercase bg-buff">
              <tr>
                <th scope="col" class="px-6 py-3">Student Name</th>
                <th scope="col" class="px-6 py-3">Student ID</th>
                <th scope="col" class="pl-6 py-3">Total Forms</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="student in filteredStudent"
                :key="student.id"
                class="bg-lightbrown border-b border-black"
              >
                <th
                  scope="row"
                  class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap"
                >
                  {{ student.first_name }} {{ student.last_name }}
                </th>
                <td class="px-6 py-4">{{ student.student_id }}</td>
                <td class="pl-6 py-4">
                  <button>{{ student.form_count }}</button>
                </td>
                <td>
                  <div class="grid grid-cols-2 gap-1"></div>
                  <button class="hover:underline" @click="view(student.id)">
                    View
                  </button>
                  <button @click="deleteStudent(student)" class="ml-2">
                    X
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
  <CreateStudent
    v-if="createStudentModal"
    :open="createStudentModal"
    @close="createStudentModal = false"
  />
</template>

<script setup>
/* eslint-disable */
// Import all the api functions for now only 1 from question.js api
import CreateStudent from "../components/CreateStudent.vue";
import { router } from "../main.js";
import axios from "axios";
import * as questionApi from "../../api/question.js";
import * as teacherApi from "../../api/teacher.js";
import * as studentApi from "../../api/student.js";
import { ref, computed } from "vue";
import { onBeforeMount, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { studentInfoStore } from "../store/student.js";
import { teacherInfoStore } from "@/store/teacherinfo";
//import { userInfoStore } from "../store/userinfo.js";
import { apiPath } from "@/constant/apiPath";
import { modalToggleStore } from "../store/modaltoggle.js";
const { createStudentModal } = storeToRefs(modalToggleStore());
const students = ref([]);
const { student } = storeToRefs(studentInfoStore());
const { teacherInfo } = storeToRefs(teacherInfoStore());
onBeforeMount(async () => {
  // students.value = await studentApi.getStudents();
  teacherInfo.value = await axios
    .get(`${apiPath()}/api/prism/get_teacher`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("AccessToken")}`,
      },
    })
    .then((res) => res?.data)
    .catch((error) => error?.response?.status);
    console.log(teacherInfo.value);
  if (
    teacherInfo.value === 404
  ) {
    await router.push("/profile");
  }
  students.value = await axios
    .get(`${apiPath()}/api/prism/get_students`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("AccessToken")}`,
      },
    })
    .then((res) => res.data)
    .catch((err) => err);
  // students.value = await studentApi.getStudents();
});

// onMounted( () => {
//   if(!localStorage.getItem("AccessToken"))
//   {
//     location.reload();
//   }
// });
const deleteStudent = async (student) => {
  const confirm = window.confirm(
    `Delete ${
      student.first_name + " " + student.last_name
    } and their existing forms?`
  );
  if (confirm) {
    // await studentApi.deleteStudent(student.id);
    await axios
      .delete(`${apiPath()}/api/prism/delete_student/${student.id}/`, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("AccessToken")}`,
        },
      })
      .then((res) => res?.data)
      .catch((error) => error?.response?.status);
    students.value = await axios
      .get(`${apiPath()}/api/prism/get_students`, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("AccessToken")}`,
        },
      })
      .then((res) => res.data)
      .catch((err) => err);
  }
};

//const { teacher } = storeToRefs(userInfoStore());
const input = ref("");
const user = ref([]);
user.value = {
  name: "Dr. Rabbit",
  school: "Whitworth High School",
};
const view = async (data) => {
  const serialize = await axios
    .get(`${apiPath()}/api/prism/get_student/${data}/`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("AccessToken")}`,
      },
    })
    .then((res) => res?.data)
    .catch((error) => error?.response?.status);
  // const serialize = await studentApi.getStudent(data);
  student.value = serialize[0];
  await router.push("/student");
};

// students.value = [
//   { name: "John Doe", student_id: "2231123", formCount: "3" },
//   { name: "Tom Cruise", student_id: "2231124", formCount: "3" },
//   { name: "John Cena", student_id: "2231125", formCount: "3" },
// ];

const filteredStudent = computed(() => {
  const data = Object.values(students.value).filter(
    (student) => {
      const firstLastName =
        student?.first_name.toLowerCase() +
        " " +
        student?.last_name.toLowerCase();
      const lastFirstName =
        student?.last_name.toLowerCase() +
        " " +
        student?.first_name.toLowerCase();
      return (
        firstLastName.includes(input.value.toLowerCase()) ||
        lastFirstName.includes(input.value.toLowerCase()) ||
        student.student_id.includes(input.value.toLocaleLowerCase())
      );
      // Code below will work once student id is not null -> Michael L
      // Backend fixed from early April -> Michael L
      // ||student?.student_id.toLowerCase().includes(input.value.toLowerCase())
    }
    // student?.first_name.toLowerCase().includes(input.value.toLowerCase()) ||
    // student?.last_name.toLowerCase().includes(input.value.toLowerCase())
    //||student?.student_id.toLowerCase().includes(input.value.toLowerCase())
  );
  return data;
});
</script>
