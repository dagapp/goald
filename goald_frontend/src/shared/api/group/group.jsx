import axios from "axios";
import { API_URL } from "@shared/consts";

export async function getUserGroups() {
  try {
    const response = await axios
      .get(API_URL + "?resultsPerPage=10")
      .then((response) => response.data);
    return response;
  } catch (error) {
    console.error(error);
  }
}
