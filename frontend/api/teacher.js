import { apiPath } from "@/constant/apiPath";
import axios from "axios";

const teacherApi = axios.create({
  baseURL: `${apiPath()}/api/prism/`,
  headers: { Authorization: `Bearer ${localStorage.getItem("AccessToken")}` },
});

export async function getTeacherInfo() {
  try {
    let { data } = await teacherApi.get("get_teacher");
    return data;
  } catch (error) {
    return error;
  }
}

export async function updateTeacherInfo(info) {
  try {
    let { data } = await teacherApi.post("update_teacher", info);
    return data;
  } catch (error) {
    return error;
  }
}
