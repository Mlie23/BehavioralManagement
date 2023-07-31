export const apiPath = () => {
  if (typeof window !== "undefined") {
    if (window.location.origin !== "http://localhost:8080") {
      return window.location.origin;
    } else {
      return "http://localhost:8000";
    }
  }
};
//export const apiPath = "http://127.0.0.1:8000";
