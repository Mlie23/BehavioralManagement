import { userStateStore } from "../src/store/userstate.js";
// import { tokenStore } from "../src/store/token.js";
import { studentInfoStore } from "@/store/student.js";
import { storeToRefs } from "pinia";
import { router } from "../src/constant/routes.js";
import { apiPath } from "@/constant/apiPath";
import axios from "axios";
// import * as studentApi from "../api/student.js";
// import { questionnaireApi } from "../api/question.js";
// import {questionnaireApi} from "../api/question.js";
export const logout = async () => {
  const { isAuthenticated } = storeToRefs(userStateStore());
  const { student } = storeToRefs(studentInfoStore());

  localStorage.clear();
  isAuthenticated.value = false;
  student.value = {};
  // questionnaireApi. = "";
  //For Emma: Add code to remove tokens from pinia!
  //Example: usertokens = {};
  //This will clear the token.
  await router.push("/");
};

const refresh_token = async () => {
  await axios
    .post(`${apiPath()}/dj-rest-auth/token/refresh/`, {
      token: `${localStorage?.getItem("RefreshToken")}`,
    })
    .then(async (res) => {
      localStorage.setItem("AcessToken", res?.data?.access_token);
      localStorage.setItem("RefreshToken", res?.data?.refresh_token);
    })
    .catch(async () => await logout());
};

export const check_authen = async () => {
  await axios
    .post(`${apiPath()}/dj-rest-auth/token/verify/`, {
      token: `${localStorage?.getItem("AccessToken")}`,
    })

    .then((res) => res.data) // User is authenticated
    .catch(async () => await refresh_token());
};
