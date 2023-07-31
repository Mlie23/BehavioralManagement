<template>
  <TransitionRoot :show="props.open">
    <Dialog @close="editStudentModal = false" class="fixed">
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
                  @click="editStudentModal = false"
                  class="absolute right-0 w-10 h-10"
                >
                  <img src="../assets/close.png" />
                </button>
                <div class="px-6 py-6">
                  <form @submit="onSubmit">
                    <!--    <form>-->

                    <h1 class="text-3xl mb-8 text-center">Edit Student</h1>
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
                    <!-- {{ student_data }} -->
                    <p>Student Name:</p>

                    <div class="grid grid-cols-2">
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
                      <p>Student ID Number</p>
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
                        <p class="text-left items-center">Student's Grade</p>
                        <select
                          v-model="grade"
                          placeholder="Select Grade"
                          class="block w-full rounded-lg border-2 border-box pl-2 py-2"
                          :class="{ 'border border-red-500': errors.grade }"
                        >
                          <option
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
                        <p>Student's Gender</p>
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
                    <div class="w-full flex justify-center items-center">
                      <button
                        type="submit"
                        class="block grid place-items-center justify-center inline-block mt-3 px-6 py-2.5 text-black font-medium text-lg bg-cornsilk hover:underline leading-tight rounded shadow-md hover:bg-blue-700 hover:shadow-lg active:bg-blue-800 active:shadow-lg"
                      >
                        Create
                      </button>
                      <!-- <button
                      @click="deleteStudent()"
                        type="delete"
                        class="ml-2 block grid place-items-center justify-center inline-block mt-3 px-6 py-2.5 text-black font-medium text-lg bg-cornsilk hover:underline leading-tight rounded shadow-md hover:bg-blue-700 hover:shadow-lg active:bg-blue-800 active:shadow-lg"
                      >
                        Delete Student
                      </button> -->
                    </div>
                  </form>
                </div>
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
import ErrorModalView from "../components/ErrorModalView.vue";
import {
  TransitionRoot,
  Dialog,
  DialogPanel,
  DialogTitle,
} from "@headlessui/vue";
import { useForm, useField } from "vee-validate";
import { storeToRefs } from "pinia";
import { userStateStore } from "../store/userstate.js";
import { userInfoStore } from "../store/userinfo.js";
import * as registrationApi from "../../api/registration.js";
import * as studentApi from "../../api/student.js";
import { router } from "../main.js";
import { ChevronDownIcon } from "@heroicons/vue/20/solid";
import VueDatePicker from "@vuepic/vue-datepicker";
import "@vuepic/vue-datepicker/dist/main.css";
// Yup behaves like regex (find things in the string)
// It is pretty neat and helpful to use yup
// It can identifies email, requirement, and you can create your own rules (using regex and dependence of other fields)
// Any question, send me a text!
import * as yup from "yup";
import { ref } from "vue";
import moment from "moment";
import VueTailwindDatepicker from "vue-tailwind-datepicker";
import { studentInfoStore } from "../store/student.js";
const { student } = storeToRefs(studentInfoStore());
import { modalToggleStore } from "../store/modaltoggle.js";
const { editStudentModal } = storeToRefs(modalToggleStore());
// const { userinfo } = storeToRefs(userInfoStore());
// const deleteStudent = async () => {
//   await studentApi.deleteStudent(student.id);
//   emit('close');
//   await router.push('/dashboard');
// };
// Create a schema that will handle the form and its rule
const emit = defineEmits("close");
const props = defineProps({
  open: { type: Boolean, required: true },
  student_data: { type: Object, required: true },
});

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
// const {value:name} = useField('name');
const { value: IEP } = false;

first_name.value = props.student_data.first_name;
last_name.value = props.student_data.last_name;
student_id.value = props.student_data.student_id;
date_of_birth.value = props.student_data.date_of_birth;
grade.value = props.student_data.grade;
gender.value = props.student_data.gender;

const errorState = ref(false);
// If requirements are passed, this button will be called
// Future purpose: Store user info and local storage
// Route user to available webpages based on their roles

const onSubmit = handleSubmit(async (values) => {
  const confirmed = window.confirm(
    `Update ${first_name.value + " " + last_name.value} information? `
  );
  if (confirmed) {
    // send api request if the user clicked Yes
    await studentApi.updateStudent(values, student.value.id);
    const serialize = await studentApi.getStudent(student.value.id);
    student.value = serialize[0];
    editStudentModal.value = false;
  }
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
