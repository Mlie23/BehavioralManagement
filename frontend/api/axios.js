// /*eslint-disable*/
// import axios from 'axios';
// import { storeToRefs } from "pinia";
// import { userInfoStore } from "../src/store/userinfo.js";
// const { userinfo } = storeToRefs(userInfoStore());
// axios.defaults.headers.common = {'Authorization': `bearer ${userinfo.access_token}`}
// export default axios;

export function getItemFromLocalStorage(key) {
  return new Promise((resolve) => {
    setTimeout(() => {
      const value = localStorage.getItem(key);
      resolve(value);
    }, 1000); // delay for 1 second
  });
}

export const AccessToken = getItemFromLocalStorage("AccessToken").then(
  (value) => {
    return value; // value of "AccessToken"
  }
);
