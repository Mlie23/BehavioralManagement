<template>
  <TransitionRoot :show="props.open">
    <Dialog @close="surveyResultModal = false" class="relative">
      <DialogPanel>
        <div
          class="fixed min-h-full inset-0 z-10 overflow-y-auto bg-gray-500/[0.95] items-center justify-center"
        >
          <div
            class="sm:w-full relative sm:mx-auto sm:max-w-6xl py-10 px-12 pb-2"
          >
            <DialogPanel id="history" class="relative">
              <div id="history" class="bg-lightbrown">
                <!-- <div>{{ questions_answered_box }}</div> -->
                <div class="flow-root text-white bg-brown px-7 py-3 text-2xl">
                  <div class="float-left">Survey Form History</div>
                  <!-- <button @click="downloadPDF('history','test')">Download</button> -->
                  <button
                    @click="surveyResultModal = false"
                    class="float-right text-xl"
                  >
                    (x)close
                  </button>
                </div>
                <!-- {{ props.answer }}
                {{ sorted_key }} -->
                <!-- :class="questionMargin(item)" -->
                <!-- {{ props.answer }} -->
                <div class="px-7" v-for="item in sorted_key" :key="item">
                  <!-- {{ question_dict[item.question]?.answers }} -->
                  {{ item }}. {{ question_dict[item]?.text }}
                  <div
                    v-for="answer in props.answer[item]"
                    :key="answer"
                    class="ml-6 font-semibold"
                  >
                    {{ answer?.text }}
                  </div>
                </div>
                <div class="flex flex-col items-center pb-2">
                  <button
                    @click="downloadPDF()"
                    class="inline-block mt-3 px-8 py-3 mb-3 bg-white font-medium text-xs leading-tight rounded-md shadow-md hover:bg-blue-700 hover:shadow-lg active:bg-blue-800 active:shadow-lg"
                  >
                    Print
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
import { ref, computed } from "vue";
import { onMounted } from "vue";
import jsPDF from "jspdf";
import html2canvas from "html2canvas";
import axios from "axios";
import { apiPath } from "@/constant/apiPath";
import { storeToRefs } from "pinia";
import { modalToggleStore } from "../store/modaltoggle.js";
const { surveyResultModal } = storeToRefs(modalToggleStore());
// import html2pdf from 'html2pdf';

// Create a reactive const to get the api return object
// const questionsApi = ref();
const questionMargin = (key) => {
  // Replace nonalphabet, count the length of curent string
  let margin = key.replace(/[^a-zA-Z]/g, "").length;
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
  answer: { type: Object, required: true },
  formId: { type: Number, required: true },
  student_name: { type: String, required: true },
});
const emit = defineEmits("close");

const loading = ref(false);
const question_dict = ref({});
// This will handle which question is displayed
const curr_active_questions = ref({});
// This will handle answers from API
const stored_answers = ref({});

//This will keep track of what answers has been pressed
const survey_results = ref({});

// handles radio logic (disallow multiple answers)
const questions_answered_box = ref({});

const downloadPDF = async () => {
  const data = await axios({
    url: `${apiPath()}/api/prism/get_form_csv/${props.formId}`,
    method: "GET",
    responseType: "blob", // important
    headers: {
      Authorization: `Bearer ${localStorage.getItem("AccessToken")}`,
    },
  })
    .then((res) => {
      const href = URL.createObjectURL(res.data);
      const link = document.createElement("a");
      link.href = href;
      link.setAttribute("download", "file.csv");
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      URL.revokeObjectURL(href);
    })
    .catch((error) => {
      return error?.response?.status;
    });
  // Creating a Blob for having a csv file format
  // and passing the data with type
  // const blob = new Blob([data], { type: 'text/csv' });

  // Creating an object for downloading url
  const url = window.URL.createObjectURL(data);

  // Creating an anchor(a) tag of HTML
  const a = document.createElement("a");

  // Passing the blob downloading url
  a.setAttribute("href", url);

  // Setting the anchor tag attribute for downloading
  // and passing the download file name
  a.setAttribute("download", "download.csv");

  // Performing a download with click
  a.click();
  // const pdf = new jsPDF();
  // const element = document.getElementById("history");
  // html2canvas(element, {
  //   useCORS: true,
  //   allowTaint: true,
  //   scale: 2,
  // }).then((canvas) => {
  //   const pdf = new jsPDF();
  //   const imgData = canvas.toDataURL("image/png");
  //   const imgProps = pdf.getImageProperties(imgData);
  //   const pdfWidth = pdf.internal.pageSize.getWidth();
  //   const pdfHeight = (imgProps.height * pdfWidth) / imgProps.width;
  //   pdf.addImage(
  //     imgData,
  //     "PNG",
  //     0,
  //     0,
  //     pdfWidth,
  //     pdf.internal.pageSize.getHeight() + 50
  //   );
  //   pdf.save(`${props.student_name}_id_${props.formId}.pdf`);
  // });
};

function printElementById(elementId) {
  // Get the HTML element
  const element = document.getElementById(elementId);

  // Create a new window to print the element
  const printWindow = window.open("", "Print Window");

  // Write the element's HTML to the new window
  printWindow.document.write(element.outerHTML);

  // Wait for the new window to finish loading
  printWindow.onload = function () {
    // Print the new window
    printWindow.print();

    // Close the new window
    printWindow.close();
  };
}
// This is lifecycle hook which will be called when the Dom is mounted
// This is for reactivity reason, we can also use it with onBeforeMount
// Please see vue lifecycle documentation
const START_QUESTION = "1";
const sortKeys = (obj) => {
  return Object.keys(obj).sort(function (a, b) {
    return a.localeCompare(b, undefined, {
      numeric: true,
      sensitivity: "base",
    });
  });
};

const sorted_key = computed(() => {
  return sortKeys(props.answer);
});
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
    survey_results.value[api_values[i]?.id] = false;
  }
};
onMounted(async () => {
  loading.value = true;
  questionApi.questionnaireApi.get("question").then((res) => {
    process_question_data(res.data);
  });
  questionApi.questionnaireApi.get("answer").then((res) => {
    process_answer_data(res.data);
  });

  loading.value = false;
});

///
</script>
