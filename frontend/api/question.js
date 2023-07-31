// Any question? ask  Michael
// Localhost URL for now that goes to django exposed api port 8080
import { apiPath } from "@/constant/apiPath";
import axios from "axios";
// We use axios for simplicity of the app and api design
// For now, I put the full path of the url that can branch off depending if we have any further apis

// const data = localStorage.getItem("AccessToken");
const resolved_apiPath = apiPath();
export const questionnaireApi = axios.create({
  baseURL: `${resolved_apiPath}/api/prism`,
  headers: { Authorization: `Bearer ${localStorage.getItem("AccessToken")}` },
});

// Create a asynchronous function to get the "GET" api functions
export async function getQuestions() {
  // {data} becomes an object that takes the data parameter-> content of the api
  let { data } = await questionnaireApi.get("question");
  // Console just to see what the data return as in debugger, remove this once you guys have idea what is happening
  return data;
}
