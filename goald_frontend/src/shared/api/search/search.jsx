import {axiosClient} from "@shared/api/axiosClient"

// // Headers for CORS. Should be removed
// axios.defaults.headers.get["Access-Control-Allow-Origin"] = "*";
// axios.defaults.headers.get["Access-Control-Allow-Methods"] = "GET";
// axios.defaults.headers.get["Access-Control-Allow-Headers"] = "Content-Type, Authentication";
// axios.defaults.headers.get["Access-Control-Allow-Credentials"] = true;

export async function getResultSearch(searchString) {
  try {
    const response = await axiosClient
      .get(`/groups?id=${searchString}`)
      .then((response) => response.data);
    return response;
  } catch (error) {
    console.error(error);
  }
}