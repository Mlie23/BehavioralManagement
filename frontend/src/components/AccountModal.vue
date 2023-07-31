<template>
  <TransitionRoot :show="props.open">
    <Dialog @close="accountModal = false" class="relative">
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

                      <button @click="accountModal = false">
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
                          :errors="errors"
                          v-if="
                            errors.first_name ||
                            errors.last_name ||
                            errors.school
                          "
                        ></ErrorModalView>

                        <p>Name:</p>

                        <div class="flex flex-col-2">
                          <input
                            id="First_name"
                            v-model="first_name"
                            class="block w-full rounded-lg border-2 border-box mb-2 mr-2 pl-2 py-2"
                            placeholder="First name"
                            :class="{
                              'border-red-500 placeholder-red-500':
                                errors.first_name,
                            }"
                          />

                          <input
                            id="Last_name"
                            v-model="last_name"
                            class="block w-full rounded-lg border-2 border-box mb-2 mr-2 pl-2 py-2"
                            placeholder="Last name"
                            :class="{
                              'border-red-500 placeholder-red-500':
                                errors.last_name,
                            }"
                          />
                        </div>

                        <p>Enter your school:</p>

                        <input
                          id="school"
                          v-model="school"
                          class="block w-full rounded-lg border-2 border-box mb-10 pl-2 py-2"
                          placeholder="School"
                          :class="{
                            'border-red-500 placeholder-red-500': errors.school,
                          }"
                        />

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
const { accountModal } = storeToRefs(modalToggleStore());
const { teacherInfo } = storeToRefs(teacherInfoStore());

onBeforeMount(async () => {
  if (
    teacherInfo.value.first_name === "" ||
    teacherInfo.value.last_name === "" ||
    teacherInfo.value.school === ""
  ) {
  } else {
    first_name.value = teacherInfo.value.first_name;
    last_name.value = teacherInfo.value.last_name;
    school.value = teacherInfo.value.school;
  }
});

const UserSchema = yup.object().shape({
  first_name: yup
    .string()
    .required("First Name is required")
    .max(50, "Maximum character is 50"),
  last_name: yup
    .string()
    .required("Last name is required")
    .max(50, "Maximum character is 50"),
  school: yup
    .string()
    .required("School is required")
    .max(50, "Maximum character is 50"),
});

const { errors, handleSubmit } = useForm({
  validationSchema: UserSchema,
});

const props = defineProps({
  open: { type: Boolean, required: true },
});
const emit = defineEmits("close");

const errorState = ref(false);
const submitErrors = ref();

const { value: first_name } = useField("first_name");
const { value: last_name } = useField("last_name");
const { value: school } = useField("school");

const onSubmit = handleSubmit(async (values) => {
  await updateTeacher(values);
});

const updateTeacher = async (values) => {
  const data = await axios
    .post(`${apiPath()}/api/prism/update_teacher`, values, {
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
  if (data?.response?.request?.status === 404) {
    errorState.value = true;
    submitErrors.value = data.response.data;
  } else {
    errorState.value = false;
    teacherInfo.value = values;
    accountModal.value = false;
    // location.reload();
    // router.push("/profile");
  }
};
</script>
