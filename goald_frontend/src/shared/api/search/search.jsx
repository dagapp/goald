import { API_URL } from "@shared/consts";

export async function getResultSearch(searchString) {
  // Possible Vuln
  const response = await fetch(API_URL + searchString, { method: "GET" })
    .then((response) => response.json())
    .then((data) => data)
    .catch((error) => {
      console.error(error);
    });

  return response;
}
