import axios from "axios";

export const axiosClient = axios.create({
  baseURL: `http://192.168.64.131:3000`,
});
