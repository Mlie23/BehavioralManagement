<template>
  <TransitionRoot :show="props.open">
    <Dialog @close="createStudentModal = false" class="fixed">
      <DialogPanel>
        <div
          class="fixed inset-0 z-10 flex w-full items-center justify-center py-12 bg-gray-500/[0.8]"
        >
          <!-- <div class="relative"> -->
          <div class="w-full fixed sm:mx-auto sm:max-w-2xl">
            <DialogPanel class="relative">
              <div
                class="rounded shadow-2xl bg-lightbrown text-black m-5 sm:m-0 border-2 border-gray-400"
              >
                <div class="w-full h-8">
                  <button
                    type="close"
                    @click="createStudentModal = false"
                    class="sm:m-0 float-right w-8 h-8"
                  >
                    <img src="../assets/close.png" />
                  </button>
                </div>
                <form @submit="onSubmit">
                  <!--    <form>-->

                  <div class="pt-1 px-6 pb-6">
                    <div v-if="errorState">
                      <div
                        class="bg-red-500 text-white font-bold rounded-t py-1"
                      ></div>

                      <div
                        class="border border-t-0 border-red-400 rounded-b bg-red-100 px-4 py-3 text-red-700"
                      >
                        <p>Invalid Credentials</p>
                      </div>
                    </div>

                    <h1 class="text-3xl mb-4 text-center">Create Student</h1>
                    <ErrorModalView
                      v-if="
                        errors.first_name ||
                        errors.last_name ||
                        errors.student_id ||
                        errors.date_of_birth ||
                        errors.grade ||
                        errors.gender
                      "
                      :errors="errors"
                    />
                    <!-- <label> Email </label> -->
                    <!-- If email does not match yup requirement, error state will appear-->
                    <p>Student Name</p>

                    <div class="grid grid-cols-2 gap-2">
                      <div>
                        <input
                          id="first_name"
                          v-model="first_name"
                          class="block w-full rounded-lg border-2 border-box mb-2 mr-2 pl-2 py-2"
                          :class="{
                            'border border-red-500': errors.first_name,
                          }"
                          placeholder="First Name"
                        />
                      </div>
                      <div>
                        <input
                          id="last_name"
                          v-model="last_name"
                          class="block w-full rounded-lg border-2 border-box mb-2 pl-2 py-2"
                          :class="{
                            'border border-red-500': errors.last_name,
                          }"
                          placeholder="Last Name"
                        />
                      </div>
                    </div>
                    <div class="grid grid-cols-1">
                      <p>Student ID</p>
                      <input
                        type="student_id"
                        id="student_id"
                        v-model="student_id"
                        name="idRules"
                        placeholder="ID"
                        class="block w-full rounded-lg border-2 border-box pl-2 py-2"
                        :class="{
                          'border border-red-500': errors.student_id,
                        }"
                      />
                    </div>

                    <!-- If username does not match yup requirement, error state will appear -->
                    <p>Date of Birth</p>
                    <VueDatePicker
                      :class="{
                        'border-2 rounded-lg border-box border-red-500':
                          errors.date_of_birth,
                      }"
                      placeholder="MM/DD/YYYY"
                      v-model="date_of_birth"
                      :enable-time-picker="false"
                      :max-date="new Date()"
                    ></VueDatePicker>

                    <div class="grid grid-cols-2 gap-1">
                      <div>
                        <p class="text-left items-center">Student Grade</p>
                        <select
                          v-model="grade"
                          placeholder="Select Grade"
                          class="block w-full rounded-lg border-2 border-box pl-2 py-2"
                          :class="{ 'border border-red-500': errors.grade }"
                        >
                          <option
                            placeholder="Select Grade"
                            v-for="standing in classStanding"
                            :key="standing.value"
                            :value="standing.value"
                            :selected="standing.current"
                          >
                            {{ standing.name }}
                          </option>
                        </select>
                      </div>
                      <div>
                        <p>Student Gender</p>
                        <input
                          type="gender"
                          id="gender"
                          v-model="gender"
                          name="idRules"
                          placeholder="Gender"
                          class="block w-full rounded-lg border-2 border-box pl-2 py-2"
                          :class="{ 'border border-red-500': errors.gender }"
                        />
                      </div>
                    </div>
                    <div class="flex flex-col items-center">
                      <button
                        type="submit"
                        class="block grid place-items-center justify-center inline-block mt-3 px-6 py-2.5 text-black font-medium text-lg bg-cornsilk hover:underline leading-tight rounded shadow-md hover:bg-blue-700 hover:shadow-lg active:bg-blue-800 active:shadow-lg"
                      >
                        Create
                      </button>
                    </div>
                  </div>
                </form>
              </div>
            </DialogPanel>
            <!-- </div> -->
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
  DialogTitle,
} from "@headlessui/vue";
import ErrorModalView from "../components/ErrorModalView.vue";
import { useForm, useField } from "vee-validate";
import { storeToRefs } from "pinia";
import { userStateStore } from "../store/userstate.js";
import * as registrationApi from "../../api/registration.js";
import * as studentApi from "../../api/student.js";
import { router } from "../main.js";
import { ChevronDownIcon } from "@heroicons/vue/20/solid";
import VueDatePicker from "@vuepic/vue-datepicker";
import "@vuepic/vue-datepicker/dist/main.css";
import axios from "axios";
import { apiPath } from "@/constant/apiPath";
// Yup behaves like regex (find things in the string)
// It is pretty neat and helpful to use yup
// It can identifies email, requirement, and you can create your own rules (using regex and dependence of other fields)
// Any question, send me a text!
import * as yup from "yup";
import { ref } from "vue";
import moment from "moment";
import VueTailwindDatepicker from "vue-tailwind-datepicker";
import { modalToggleStore } from "../store/modaltoggle.js";
const { createStudentModal } = storeToRefs(modalToggleStore());
const { isAuthenticated } = storeToRefs(userStateStore());
// Create a schema that will handle the form and its rule

const props = defineProps({
  open: { type: Boolean, required: true },
});
const emit = defineEmits("close");
const RegisterSchema = yup.object().shape({
  first_name: yup.string().required("First Name is required"),
  last_name: yup.string().required("Last Name is required"),
  student_id: yup.string().required("Student ID is required"),
  // date_of_birth: yup.string().required("Date of Birth is required"),
  grade: yup.string().required("Grade is required"),
  gender: yup
    .string()
    .required("Gender is required")
    .matches(/^[aA-zZ\s]+$/, "Only alphabets are allowed for Gender field "),
});

// Inject errors and submit dependency to our form
const { errors, handleSubmit } = useForm({
  validationSchema: RegisterSchema,
});

const { value: first_name } = useField("first_name");
const { value: last_name } = useField("last_name");
const { value: student_id } = useField("student_id");
const { value: date_of_birth } = useField("date_of_birth");
const { value: grade } = useField("grade");
const { value: gender } = useField("gender");
const { value: IEP } = false;

const errorState = ref(false);
// If requirements are passed, this button will be called
// Future purpose: Store user info and local storage
// Route user to available webpages based on their roles

const onSubmit = handleSubmit(async (values) => {
  await axios.post(`${apiPath()}/api/prism/create_student`, values, {
    headers: {
      Authorization: `Bearer ${localStorage.getItem("AccessToken")}`,
    },
  });
  createStudentModal.value = false;
  location.reload();
});

const classStanding = [
  { name: "Kindergarten", value: "Kindergarten", current: false },
  { name: "1st Grade", value: "1st Grade" },
  { name: "2nd Grade", value: "2nd Grade" },
  { name: "3rd Grade", value: "3th Grade" },
  { name: "4th Grade", value: "4th Grade" },
  { name: "5th Grade", value: "5th Grade" },
  { name: "6th Grade", value: "6th Grade" },
  { name: "7th Grade", value: "7th Grade" },
  { name: "8th Grade", value: "8th Grade" },
  { name: "9th Grade", value: "9th Grade" },
  { name: "10th Grade", value: "10th Grade" },
  { name: "11th Grade", value: "11th Grade" },
  { name: "12th Grade", value: "12th Grade" },
];
</script>
