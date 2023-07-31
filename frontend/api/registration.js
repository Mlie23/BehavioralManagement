/*eslint-disable*/
import { apiPath } from "@/constant/apiPath";
import axios from "axios";
const registrationApi = axios.create({
  baseURL: `${apiPath()}`,
});

export async function register(info) {
  try {
    let { data } = await registrationApi.post(
      "dj-rest-auth/registration/",
      info
    );
    return data;
  } catch (error) {
    return error;
  }
}

export async function login(info) {
  try {
    let { data } = await registrationApi.post("dj-rest-auth/login/", info);
    return data;
  } catch (error) {
    return error;
  }
}
