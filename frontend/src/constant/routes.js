/*eslint-disable*/
import FormView from "../components/ResultView.vue";
import LandingView from "../components/LandingView.vue";
// import SurveyView from "../components/SurveyView.vue";
import ErrorView from "../components/ErrorView.vue";
import LoginView from "../components/LoginView.vue";
import InformationView from "../components/InformationView.vue";
import CreateAccount from "../components/CreateAccount.vue";
import DashboardView from "../components/DashboardView.vue";
import StudentForm from "../components/CreateStudent.vue";
import StudentView from "../components/StudentView.vue";
import MyProfile from "../components/MyProfile.vue";
import SurveyResultModal from "../components/SurveyResultModal.vue";
import RegistrationRedirect from "../components/RegistrationRedirect.vue";
import { createWebHistory, createRouter } from "vue-router";
import { userStateStore } from "@/store/userstate";
import { storeToRefs } from "pinia";
import { teacherInfoStore } from "@/store/teacherinfo";

const routerHistory = createWebHistory();
export var ROUTES = [
  { path: "/", component: LandingView, meta: { requireAuth: false } },
  // { path: "/survey", component: SurveyView, meta: { requireAuth: true } },
  { path: "/result", component: FormView, meta: { requireAuth: true } },
  { path: "/login", component: LoginView, meta: { requireAuth: false } },
  {
    path: "/createaccount",
    component: CreateAccount,
    meta: { requireAuth: false },
  },
  { path: "/dashboard", component: DashboardView, meta: { requireAuth: true } },
  { path: "/info", component: InformationView, meta: { requireAuth: true } },
  {
    path: "/:pathMatch(.*)*",
    component: ErrorView,
    meta: { requireAuth: false },
  },
  {
    path: "/createstudent",
    component: StudentForm,
    meta: { requireAuth: true },
  },
  { path: "/student", component: StudentView, meta: { requireAuth: true } },
  {
    path: "/profile",
    component: MyProfile,
    meta: { requireAuth: true },
  },
  {
    path: "/registrationredirect",
    component: RegistrationRedirect,
    meta: { requireAuth: false },
  },
  {
    path: "/res",
    component: SurveyResultModal,
    meta: { requireAuth: true },
  },
];

const router = createRouter({
  history: routerHistory,
  routes: ROUTES,
});

router.beforeEach((to, from, next) => {
  const { teacherInfo } = storeToRefs(teacherInfoStore());
  const { isAuthenticated } = storeToRefs(userStateStore());
  if (
    isAuthenticated.value &&
    (to.path == "/login" || to.path == "/" || to.path == "/createaccount")
  ) {
    next({ path: "/dashboard" });
  }
  if (
    // make sure the user is authenticated
    !isAuthenticated.value &&
    to.meta.requireAuth
  ) {
    // redirect the user to the login page
    next({ path: "/login" });
  } else {
    next();
  }
});

export { router };
