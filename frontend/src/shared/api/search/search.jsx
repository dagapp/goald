import {axiosClient} from "@shared/api/axiosClient"

export async function getResultSearch(searchString) {
  try {
    const response = await axiosClient
      .get(`/group?name=${searchString}`)
      .then((response) => response.data);
    return response;
  } catch (error) {
    console.error(error);
  }
}