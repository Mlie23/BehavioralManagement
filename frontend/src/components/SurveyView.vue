<template>
  <TransitionRoot :show="props.open">
    <Dialog @close="surveyModal = false" class="relative">
      <DialogPanel>
        <div
          class="fixed h-full inset-0 z-10 overflow-y-auto bg-gray-500/[0.95] items-center justify-center"
        >
          <div
            class="sm:w-full relative sm:mx-auto sm:max-w-6xl py-10 px-12 pb-2"
          >
            <DialogPanel class="relative">
              <div class="bg-lightbrown">
                <!-- <div>{{ questions_answered_box }}</div> -->
                <div class="flow-root text-white bg-brown px-7 py-3 text-2xl">
                  <div class="float-left">FBA Form</div>
                  <button
                    @click="surveyModal = false"
                    class="float-right text-xl"
                  >
                    (x)close
                  </button>
                </div>
                <!-- <p>1: {{getAnswerArray()}}</p>
                <p>2:{{ get_answers}} </p>
                <p>3:{{ get_active_question_answers }}</p>
                <p>4:{{ questions_answered_box }}</p> -->
                <div
                  class="px-7"
                  v-for="(key, index) in sorted_key"
                  :key="key.id"
                >
                  <div
                    v-if="
                      curr_active_questions[key] === true &&
                      index != sorted_key.length - 1
                    "
                    :class="questionMargin(key)"
                  >
                    <!-- <p>index{{ index }} {{ sorted_key.length-1 }}</p> -->
                    <p class="text-l text-gray-500 font-semibold">
                      {{ key }}. {{ question_dict[key]?.text }}
                    </p>
                    <div v-if="question_dict[key].multiple_choice === true">
                      <div
                        v-for="answers in question_dict[key].answers"
                        :key="answers.id"
                        class="ml-5"
                      >
                        <div v-if="stored_answers[answers]?.is_other === true">
                          <input
                            type="checkbox"
                            :id="answers"
                            :value="answers"
                            :name="answers"
                            v-model="
                              questions_answered_box[
                                question_dict[key]?.question_number
                              ]
                            "
                            @change="adjust_active_question_radio"
                          />
                          <label class="ml-1" for="checkbox">{{
                            stored_answers[answers]?.text
                          }}</label>
                          <!-- {{ getAnswerArray(stored_answers[answers].id) }} -->

                          <!-- {{ stored_answers[answers].id }} -->
                          <!-- <div>{{stored_answers[asnwers]?.is_other}}</div> -->
                          <textarea
                            v-if="getAnswerArray(stored_answers[answers].id)"
                            v-model="custom_answers[answers]"
                            id="message"
                            rows="1"
                            class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500"
                            placeholder="Other input..."
                          ></textarea>
                          <!-- <textarea

                            placeholder="Click the checkbox after you are finished with your answer"
                          ></textarea> -->
                        </div>
                        <div v-else>
                          <input
                            type="checkbox"
                            :id="answers"
                            :value="answers"
                            :name="answers"
                            v-model="
                              questions_answered_box[
                                question_dict[key]?.question_number
                              ]
                            "
                            @change="adjust_active_question_radio"
                          />
                          <label class="ml-1" for="checkbox">{{
                            stored_answers[answers]?.text
                          }}</label>
                        </div>
                      </div>
                    </div>
                    <div v-else>
                      <div
                        v-for="answers in question_dict[key].answers"
                        :key="answers.id"
                        class="ml-5"
                      >
                        <div v-if="stored_answers[answers]?.is_other === true">
                          <input
                            type="radio"
                            :id="answers"
                            :value="answers"
                            :name="answers"
                            v-model="
                              questions_answered_box[
                                question_dict[key].question_number
                              ]
                            "
                            @change="adjust_active_question_radio"
                          />
                          <label class="ml-1" for="radio">{{
                            stored_answers[answers]?.text
                          }}</label>
                          <div>{{ stored_answers[asnwers]?.is_other }}</div>
                          <textarea
                            v-model="custom_answers[answers]"
                            id="message"
                            rows="2"
                            class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500"
                            placeholder="Other..."
                          ></textarea>
                          <!-- <textarea
                            v-model="custom_answers[answers]"
                            placeholder="Click the checkbox after you are finished with your answer"
                          ></textarea> -->
                        </div>
                        <div v-else>
                          <input
                            type="radio"
                            :id="answers"
                            :value="answers"
                            :name="answers"
                            v-model="
                              questions_answered_box[
                                question_dict[key].question_number
                              ]
                            "
                            @change="adjust_active_question_radio"
                          />
                          <label class="ml-1" for="radio">{{
                            stored_answers[answers]?.text
                          }}</label>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="flex flex-col items-center pb-2">
                  <!-- @click="router.push('/result')" -->
                  <button
                    @click="onSubmit"
                    v-if="curr_active_questions['END'] === true"
                    class="inline-block mt-3 px-8 py-3 bg-white font-medium text-xs leading-tight rounded-md shadow-md hover:bg-blue-700 hover:shadow-lg active:bg-blue-800 active:shadow-lg"
                  >
                    Submit
                  </button>
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
  DialogTitle,
} from "@headlessui/vue";
// Import all the api functions for now only 1 from question.js api
import * as questionApi from "../../api/question.js";
import * as studentApi from "../../api/student.js";
import { ref, computed, toRaw } from "vue";
import { storeToRefs } from "pinia";
import { onMounted } from "vue";
import { router } from "../main.js";
import axios from "axios";
import { apiPath } from "@/constant/apiPath";
import { modalToggleStore } from "@/store/modaltoggle";
const { surveyModal } = storeToRefs(modalToggleStore());
const get_answers = computed(() => {
  let answerarray = [];
  let arr = get_active_question_answers.value;
  for (var i = 0; i < arr.length; i++) {
    let temp = arr[i][1];
    if (Array.isArray(temp)) {
      answerarray.splice(1, 0, ...temp);
    } else {
      answerarray.push(temp);
    }
  }
  return answerarray;
});

const get_active_question_answers = computed(() => {
  const new_array = Object.entries(questions_answered_box.value);
  return new_array.filter((x) => {
    return curr_active_questions.value[x[0]];
  });
});

const getAnswerArray = (question) => {
  const new_array = Object.entries(questions_answered_box.value);
  new_array.filter((x) => {
    return curr_active_questions.value[x[0]];
  });
  let answerarray = [];
  let arr = new_array;
  for (var i = 0; i < arr.length; i++) {
    let temp = arr[i][1];
    if (Array.isArray(temp)) {
      answerarray.splice(1, 0, ...temp);
    } else {
      answerarray.push(temp);
    }
  }
  for (i = 0; i < answerarray.length; i++) {
    if (answerarray[i] === question) {
      return true;
    }
  }
  return false;
};
const onSubmit = async () => {
  // const answerarray = Array.from(
  //   Object.values(get_active_question_answers())
  // );
  let answerarray = [];
  let arr = get_active_question_answers.value;
  for (var i = 0; i < arr.length; i++) {
    let temp = arr[i][1];
    if (Array.isArray(temp)) {
      answerarray.splice(1, 0, ...temp);
    } else {
      answerarray.push(temp);
    }
  }
  let values = {
    student: props.student_id,
    answers: answerarray,
    custom_answers: custom_answers.value,
  };
  await studentApi.createForm(values);
  surveyModal.value = false;
  location.reload();
};
// Create a reactive const to get the api return object
// const questionsApi = ref();
const questionMargin = (key) => {
  // Replace nonalphabet, count the length of curent string
  let new_key = key.replace("ALT", "");
  new_key = new_key.replace(" ", "");
  let margin = new_key.replace(/[^a-zA-Z]/g, "").length;
  if (margin == 1) {
    return "ml-5";
  } else if (margin > 1) {
    return "ml-10";
  } else {
    return "";
  }
};

const props = defineProps({
  open: { type: Boolean, required: true },
  student_id: { type: Number, required: true },
});
const emit = defineEmits("close");

const loading = ref(false);
const question_dict = ref({});
// This will handle which question is displayed
const curr_active_questions = ref({});
// This will handle answers from API
const stored_answers = ref({});

// //This will keep track of what answers has been pressed
// const survey_results = ref({});

// handles radio logic (disallow multiple answers)
const questions_answered_box = ref({});

// handles custom/other answers
const custom_answers = ref({});

const sorted_key = computed(() => {
  return sortKeys(curr_active_questions.value);
});

// This is lifecycle hook which will be called when the Dom is mounted
// This is for reactivity reason, we can also use it with onBeforeMount
// Please see vue lifecycle documentation
const START_QUESTION = "1";
const sortKeys = (obj) => {
  const keys = Object.keys(obj).sort((a, b) => {
    const aNum = parseInt(a);
    const bNum = parseInt(b);
    const aAlpha = a.replace("ALT", "").replace(/[^a-z]/gi, "");
    const bAlpha = b.replace("ALT", "").replace(/[^a-z]/gi, "");

    if (isNaN(aNum) || isNaN(bNum)) {
      return a.localeCompare(b);
    } else if (aNum !== bNum) {
      return aNum - bNum;
    } else if (aAlpha !== bAlpha) {
      return aAlpha.localeCompare(bAlpha);
    } else {
      return a.localeCompare(b);
    }
  });
  return keys;
};

const process_question_data = (api_values) => {
  for (let i = 0; i < api_values?.length; i++) {
    question_dict.value[api_values[i]?.question_number] = api_values[i];
    curr_active_questions.value[api_values[i]?.question_number] = false;
    questions_answered_box.value[api_values[i]?.question_number] = [];
  }
  curr_active_questions.value[START_QUESTION] = true;
};

const process_answer_data = (api_values) => {
  for (let i = 0; i < api_values?.length; i++) {
    stored_answers.value[api_values[i]?.id] = api_values[i];
    // survey_results.value[api_values[i]?.id] = false;
    custom_answers.value[api_values[i]?.id] = [];
  }
};
onMounted(async () => {
  loading.value = true;
  await axios
    .get(`${apiPath()}/api/prism/question`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("AccessToken")}`,
      },
    })
    .then((res) => process_question_data(res.data))
    .catch((error) => error);
  await axios
    .get(`${apiPath()}/api/prism/answer`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("AccessToken")}`,
      },
    })
    .then((res) => process_answer_data(res.data))
    .catch((error) => error);
  // questionApi.questionnaireApi.get("question").then((res) => {
  //   process_question_data(res.data);
  // });
  // questionApi.questionnaireApi.get("answer").then((res) => {
  //   process_answer_data(res.data);
  // });

  loading.value = false;
});

const adjust_active_question_radio = (event) => {
  // reset curr_active questions
  for (const [key, value] of Object.entries(curr_active_questions.value)) {
    curr_active_questions.value[key] = false;
  }
  curr_active_questions.value[START_QUESTION] = true;

  /// new logic for question display
  // first, start with question 0
  var stack = [];
  stack.push(question_dict.value[START_QUESTION]);
  // add the id to set
  var visited = new Set();
  // get the current active answers for this question
  //WOW, BFS! I know! What an application!
  while (stack.length > 0) {
    const curr_question = stack.pop();
    if (curr_question !== null && curr_question !== undefined) {
      if (!(curr_question.question_number in visited)) {
        const curr_question_answers = toRaw(
          questions_answered_box.value[curr_question.question_number]
        ); // make it not proxy, but a raw array or int
        if (curr_question_answers !== []) {
          // the curr_question_answers can either be a single number for non-multiple choice, and an array for multiple choice. I hate Vue. I can't beleive React is better fr fr.
          // No one is gonna read this, so buy Lobotomy Corporation at https://store.steampowered.com/app/568220/Lobotomy_Corporation__Monster_Management_Simulation/
          if (Number.isInteger(curr_question_answers)) {
            const the_next_question =
              stored_answers.value[curr_question_answers].next_question;
            if (the_next_question !== null && the_next_question !== undefined) {
              curr_active_questions.value[the_next_question] = true;
              stack.push(question_dict.value[the_next_question]);
            }
          } else {
            for (let i = 0; i < curr_question_answers.length; i++) {
              const the_next_question =
                stored_answers.value[curr_question_answers[i]].next_question;
              if (
                the_next_question !== null &&
                the_next_question !== undefined
              ) {
                curr_active_questions.value[the_next_question] = true;
                stack.push(question_dict.value[the_next_question]);
              }
            }
          }
        }
      }
      visited.add(curr_question.question_number);
    }
  }
  ///
};
</script>
