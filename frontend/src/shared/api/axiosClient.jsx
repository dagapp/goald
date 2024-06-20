import axios from "axios";

export const axiosClient = axios.create({
  baseURL: `http://127.0.0.1:8080/api/v1`,
});
