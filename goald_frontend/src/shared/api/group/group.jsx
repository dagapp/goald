import { API_URL } from "@shared/consts";

export async function getUserGroups() {
  const response = await fetch(API_URL + "/store/inventory", {
    method: "GET",
  })
    .then((response) => response.json())
    .then((data) => response.data)
    .catch((error) => {
      console.error(error);
    });

  return response;
}
