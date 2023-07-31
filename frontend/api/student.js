import { apiPath } from "@/constant/apiPath";
import axios from "axios";
// import { interceptor } from "./interceptor";
// import { getItemFromLocalStorage } from "./axios";
// getItemFromLocalStorage("AccessToken");

const studentApi = axios.create({
  baseURL: `${apiPath()}/api/prism/`,
  headers: { Authorization: `Bearer ${localStorage.getItem("AccessToken")}` },
});
// studentApi.interceptors.request.use(interceptor);
export async function getStudents() {
  try {
    let { data } = await studentApi.get("get_students");
    return data;
  } catch (error) {
    return error;
  }
}

export async function getStudent(student_id) {
  try {
    let { data } = await studentApi.get(`get_student/${student_id}`);
    return data;
  } catch (error) {
    return error;
  }
}

export async function getForms(student_id) {
  try {
    let { data } = await studentApi.get(`get_student_forms/${student_id}`);
    return data;
  } catch (error) {
    return error;
  }
}

export async function getForm(formId) {
  let { data } = await studentApi.get(`get_form/${formId}`);
  return data;
}

export async function createStudent(info) {
  try {
    let { data } = await studentApi.post(`create_student`, info);
    return data;
  } catch (error) {
    return error?.response?.status;
  }
}

export async function updateStudent(info, pk) {
  try {
    let { data } = await studentApi.post(`update_student/${pk}/`, info);
    return data;
  } catch (error) {
    return error.response.status;
  }
}

export async function deleteStudent(student_id) {
  try {
    let { data } = await studentApi.delete(`delete_student/${student_id}`);
    return data;
  } catch (error) {
    return error.response.status;
  }
}

export async function createForm(info) {
  try {
    let { data } = await studentApi.post("create_form", info);
    return data;
  } catch (error) {
    return error.response.status;
  }
}
