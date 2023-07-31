/* eslint-disable */
import { createApp } from "vue";
import App from "./App.vue";
import "./index.css";
import { createPinia } from "pinia";
import FormView from "./components/ResultView.vue";
import LandingView from "./components/LandingView.vue";
import SurveyView from "./components/SurveyView.vue";
import ErrorView from "./components/ErrorView.vue";
import piniaPluginPersistedstate from "pinia-plugin-persistedstate";
import { router } from "./constant/routes.js";
import { modalToggleStore } from "./store/modaltoggle";
// const  token  = localStorage.getItem('_utoken');
// if (!to.meta.public)
// {
//   // page requires authentication - if there is none, redirect to /login
//   if (token) next();
//   else next('/login');
// }
// else
// {
//   // Login is supposedly public - skip navigation if we have a token
//   if (token ? to.path !== '/login' : true) next();
// }
const pinia = createPinia();
pinia.use(piniaPluginPersistedstate);
const app = createApp(App);
app.use(pinia).use(router);

app.mount("#app");
export { router };
