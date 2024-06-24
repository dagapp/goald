import axios from "axios";

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

export const axiosClient = axios.create({
  baseURL: `http://127.0.0.1:80/api/v1`,
});
