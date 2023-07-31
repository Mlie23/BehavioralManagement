<template>
  <div class="bg-cornsilk flex h-full w-full flex-col justify-center">
    <div class="sm:mx-auto sm:w-full sm:max-w-7xl px-3 pt-5">
      <div class="grid sm:grid-cols-4 grid-cols-4 gap-4 sm:gap-12">
        <div
          class="sm:col-start-2 sm:col-span-2 col-span-4 rounded-lg flex flex-col items-center bg-lightbrown"
        >
          <div class="rounded-lg w-full py-5 bg-buff"></div>
          <!-- {{ formInfo.answers }} -->
          <!-- {{ answers }} -->
          <!-- {{ student }} -->
          <div class="text-3xl font-semibold pt-3">
            <!-- {{ formInfo.id }} -->
            {{ student.first_name }} {{ student.last_name }} Summary
          </div>
          <div
            class="font-semibold w-full text-md text-center sm:px-10 pt-1 flow-root"
          >
            Grade: {{ student.grade }}
          </div>
          <div class="font-semibold w-full text-md text-center sm:px-10 pt-1">
            Gender: {{ student.gender }}
          </div>
          <div class="font-semibold w-full text-md text-center sm:px-10 pt-1">
            Date: {{ trimDate(formInfo?.date) }}
          </div>
          <div class="font-semibold w-full text-md text-center sm:px-10 pt-1">
            Form ID: {{ formInfo.id }}
          </div>
          <!-- <div class="flex items-center text-left sm:px-10 pt-1">
            1. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris
          </div>
          <div class="flex items-center text-left sm:px-10 pt-1">
            2. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris
          </div>
          <div class="flex items-center text-left sm:px-10 pt-1">
            3. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris
          </div> -->
        </div>
        <div
          class="rounded-lg col-span-4 flex flex-col items-center bg-lightbrown pb-4"
        >
          <div class="w-full py-5 bg-buff rounded-lg"></div>
          <div class="w-full sm:px-10">
            <div class="w-full text-md pt-1 text-center font-semibold">
              Testable Hypothesis Summary
            </div>
            <!-- <div class="w-3/4 border-b border-2 border-buff mt-3 mb-2"></div> -->
            <div class="grid grid-cols-4 bg-[#E9E7DC] text-sm">
              <div
                class="break-words text-center border border-black font-semibold"
              >
                Setting Event
              </div>
              <div
                class="break-words text-center border-black border-y border-r font-semibold"
              >
                Triggering Antecedent
              </div>
              <div
                class="break-words text-center border-black border-y border-r font-semibold"
              >
                Behavior
              </div>
              <div
                class="break-words text-center border-black border-y border-r font-semibold"
              >
                Maintaining consequence
              </div>
            </div>
            <div class="grid grid-cols-4 bg-cornsilk text-sm">
              <div class="px-2 break-words border-x border-b border-black">
                <!-- {{ answers[9][0]?.text }} -->
                <!-- {{ surveyResultDictionary.setting }} -->
                <p
                  v-for="(item, index) in surveyResultDictionary.setting"
                  :key="item"
                >
                  {{ ++index }}. {{ item }}.
                </p>
              </div>
              <div class="px-2 break-words border-black border-b border-r">
                <p
                  v-for="(item, index) in surveyResultDictionary.trigger"
                  :key="item"
                >
                  {{ ++index }}. {{ item }}.
                </p>
              </div>
              <div class="px-2 break-words border-black border-b border-r">
                <p
                  v-for="(item, index) in surveyResultDictionary.behavior"
                  :key="item"
                >
                  {{ ++index }}. {{ item }}.
                </p>
              </div>
              <div class="px-2 break-words border-black border-b border-r">
                <p
                  v-for="(item, index) in surveyResultDictionary.consequence"
                  :key="item"
                >
                  {{ ++index }}. {{ item }}.
                </p>
              </div>
            </div>

            <div class="w-full text-md pt-1 text-center font-semibold">
              Behavior Support Plan Recommendations
            </div>
            <!-- <div class="w-3/4 border-b border-2 border-buff mt-3 mb-2"></div> -->
            <div class="grid grid-cols-4 bg-[#E9E7DC] text-sm">
              <div
                class="break-words text-center border border-black font-semibold"
              >
                Setting Event
              </div>
              <div
                class="col-span-3 break-words text-center border-black border-y border-r font-semibold"
              >
                Setting Event Strategies
              </div>
              <!-- <div
                class="break-words text-center border-black border-y border-r font-semibold"
              >
                Behavior
              </div>
              <div
                class="break-words text-center border-black border-y border-r font-semibold"
              >
                Maintaining consequence
              </div> -->
            </div>
            <div class="grid grid-cols-4 bg-cornsilk text-sm">
              <div class="px-2 break-words border-x border-b border-black">
                <p
                  v-for="(item, index) in surveyResultDictionary.setting"
                  :key="item"
                >
                  {{ ++index }}. {{ item }}.
                </p>
              </div>
              <div
                class="col-span-3 px-2 break-words border-black border-b border-r"
              >
                <p
                  v-for="(
                    item, index
                  ) in surveyResultDictionary.setting_strategy"
                  :key="item"
                >
                  {{ ++index }}. {{ item }}.
                </p>
              </div>
              <!-- <div class="px-2 break-words border-black border-b border-r">
                {{ answers[3][0]?.text }}
              </div>
              <div class="px-2 break-words border-black border-b border-r">
                {{ answers[8][0]?.text }}
              </div> -->
            </div>

            <div class="grid grid-cols-4 bg-[#E9E7DC] text-sm">
              <div
                class="break-words text-center border border-black font-semibold"
              >
                Triggering Antecedent
              </div>
              <div
                class="col-span-3 break-words text-center border-black border-y border-r font-semibold"
              >
                Antecedent Strategies
              </div>
            </div>
            <div class="grid grid-cols-4 bg-cornsilk text-sm">
              <div class="px-2 break-words border-x border-b border-black">
                <p
                  v-for="(item, index) in surveyResultDictionary.trigger"
                  :key="item"
                >
                  {{ ++index }}. {{ item }}.
                </p>
              </div>
              <div
                class="col-span-3 px-2 break-words border-black border-b border-r"
              >
                <p
                  v-for="(
                    item, index
                  ) in surveyResultDictionary.trigger_strategy"
                  :key="item"
                >
                  {{ ++index }}. {{ item }}.
                </p>
              </div>
            </div>

            <div class="grid grid-cols-4 bg-[#E9E7DC] text-sm">
              <div
                class="break-words text-center border border-black font-semibold"
              >
                Behavior
              </div>
              <div
                class="col-span-3 break-words text-center border-black border-y border-r font-semibold"
              >
                Behavior Strategies
              </div>
            </div>
            <div class="grid grid-cols-4 bg-cornsilk text-sm">
              <div class="px-2 break-words border-x border-b border-black">
                <p
                  v-for="(item, index) in surveyResultDictionary.behavior"
                  :key="item"
                >
                  {{ ++index }}. {{ item }}.
                </p>
              </div>
              <div
                class="col-span-3 px-2 break-words border-black border-b border-r"
              >
                <p
                  v-for="(
                    item, index
                  ) in surveyResultDictionary.behavior_strategy"
                  :key="item"
                >
                  {{ ++index }}. {{ item }}.
                </p>
              </div>
            </div>

            <div class="grid grid-cols-4 bg-[#E9E7DC] text-sm">
              <div
                class="break-words text-center border border-black font-semibold"
              >
                Maintaining Consequence
              </div>
              <div
                class="col-span-3 break-words text-center border-black border-y border-r font-semibold"
              >
                Consequence Strategies
              </div>
            </div>
            <div class="grid grid-cols-4 bg-cornsilk text-sm">
              <div class="px-2 break-words border-x border-b border-black">
                <p
                  v-for="(item, index) in surveyResultDictionary.consequence"
                  :key="item"
                >
                  {{ ++index }}. {{ item }}.
                </p>
              </div>
              <div
                class="col-span-3 px-2 break-words border-black border-b border-r"
              >
                <p
                  v-for="(
                    item, index
                  ) in surveyResultDictionary.consequence_strategy"
                  :key="item"
                >
                  {{ ++index }}. {{ item }}.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="flex flex-row justify-center pb-5">
        <button
          @click="surveyResultModal = true"
          class="mr-2 inline-block mt-3 px-8 py-3 bg-lightbrown font-medium text-lg leading-tight rounded shadow-md hover:bg-brown hover:shadow-lg active:bg-blue-800 active:shadow-lg"
        >
          Survey History
        </button>
        <button
          @click="router.push('/dashboard')"
          class="ml-2 inline-block mt-3 px-8 py-3 bg-lightbrown font-medium text-lg leading-tight rounded shadow-md hover:bg-brown hover:shadow-lg active:bg-blue-800 active:shadow-lg"
        >
          Return to Dashboard
        </button>
      </div>
    </div>
  </div>
  <SurveyResultModal
    v-if="surveyResultModal"
    :open="surveyResultModal"
    :answer="answers"
    :formId="formInfo.id"
    :student_name="student.first_name + ' ' + student.last_name"
  />
</template>
<script setup>
/*eslint-disable*/
import SurveyResultModal from "./SurveyResultModal.vue";
import moment from "moment";
import { router } from "../main.js";
import { computed, onBeforeMount, ref } from "vue";
import { storeToRefs } from "pinia";
import { modalToggleStore } from "../store/modaltoggle.js";
const { surveyResultModal } = storeToRefs(modalToggleStore());
import { studentInfoStore } from "../store/student.js";
import * as studentApi from "../../api/student.js";
import axios from "axios";
import { apiPath } from "@/constant/apiPath.js";
const { student, formId } = storeToRefs(studentInfoStore());
const trimDate = (date) => {
  return moment(date).format("MMMM DD YYYY");
};
const formInfo = ref({});
const answers = ref();
const surveyResultDictionary = ref({
  strength: [],
  setting: [],
  locations: [],
  behavior: [],
  trigger: [],
  consequence: [],
  setting_strategy: [],
  behavior_strategy: [],
  trigger_strategy: [],
  consequence_strategy: [],
});

onBeforeMount(async () => {
  // reset
  surveyResultDictionary.value = {
    strength: [],
    setting: [],
    locations: [],
    behavior: [],
    trigger: [],
    consequence: [],
    setting_strategy: [],
    behavior_strategy: [],
    trigger_strategy: [],
    consequence_strategy: [],
  };
  const serializer = await axios
    .get(`${apiPath()}/api/prism/get_form/${formId.value}`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("AccessToken")}`,
      },
    })
    .then((res) => res?.data)
    .catch((error) => error?.response?.status);
  formInfo.value = serializer[0];
  let mergedObject = formInfo.value.answers.reduce((obj, item) => {
    if (!obj[item.question]) {
      obj[item.question] = [];
    }
    obj[item.question].push(item);
    return obj;
  }, {});
  const fixed_answers = serializer[0]?.answers;
  const custom_answers = serializer[0]?.other_answer;
  for (let i = 0; i < fixed_answers.length; i++) {
    if (fixed_answers[i]?.strength != null)
      surveyResultDictionary.value.strength.push(fixed_answers[i]?.strength);
    if (fixed_answers[i]?.setting != null)
      surveyResultDictionary.value.setting.push(fixed_answers[i]?.setting);
    if (fixed_answers[i]?.locations != null)
      surveyResultDictionary.value.locations.push(fixed_answers[i]?.locations);
    if (fixed_answers[i]?.behavior != null)
      surveyResultDictionary.value.behavior.push(fixed_answers[i]?.behavior);
    if (fixed_answers[i]?.trigger != null)
      surveyResultDictionary.value.trigger.push(fixed_answers[i]?.trigger);
    if (fixed_answers[i]?.consequence != null)
      surveyResultDictionary.value.consequence.push(
        fixed_answers[i]?.consequence
      );
    if (fixed_answers[i]?.setting_strategy != null)
      surveyResultDictionary.value.setting_strategy.push(
        fixed_answers[i]?.setting_strategy
      );
    if (fixed_answers[i]?.behavior_strategy != null)
      surveyResultDictionary.value.behavior_strategy.push(
        fixed_answers[i]?.behavior_strategy
      );
    if (fixed_answers[i]?.trigger_strategy != null)
      surveyResultDictionary.value.trigger_strategy.push(
        fixed_answers[i]?.trigger_strategy
      );
    if (fixed_answers[i]?.consequence_strategy != null)
      surveyResultDictionary.value.consequence_strategy.push(
        fixed_answers[i]?.consequence_strategy
      );
  }
  for (let i = 0; i < custom_answers.length; i++) {
    const strat_type = custom_answers[i]?.strategy_type;
    const strat_text = custom_answers[i]?.text;
    surveyResultDictionary.value[strat_type].push(strat_text);
  }
  answers.value = mergedObject;
});

const settingEventStrategies = [
  "Arrange in-depth communication and supervision",
  "Increase verbal communications and reasonings with students",
  "Easen the situation and provide comfortability",
];
const antecendentStrategies = [
  "Provide high quality attention for appropriate behavior before problem behaviors occur",
  "Prompt or precorrect new skills before the problem",
  "One-on-one check ins with preferred adult before school, class, or problematic routines",
  "Give a “job” or role that requires adult interaction",
  "Arrange proximity near adults",
  "Increase active supervision with student",
];

const behaviorStrategies = [
  "Teach student skills to recruit adult attention (ask to play, ask for help, ask for time with adult, etc.)",
];

const consequenceStrategies = [
  "Provide immediate, high quality attention for replacement behaviors (match quality and quantity to the type of attention historically experienced for problem behavior).",
  "Non-verbally redirect problem in “brief and boring” manner (reduce talking and eye contact, etc.)",
  "Arrange time with preferred adults for meeting behavioral goals",
  "Planned ignoring, (only consider for behavior that does not escalate)",
  "Provide attention to other students engaging in appropriate behavior",
  "“The Good Behavior Game”",
  "Complete preference assessment",
  "Arrange contingency contract (if-then rule or behavior contract) rewards for using newly taught skills, progress toward behavioral goals, or absence of problem behaviors.",
  "Daily behavior tracking form",
];
</script>
