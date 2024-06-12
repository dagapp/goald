import {axiosClient} from "@shared/api/axiosClient"

// export async function getUserGroups(id) {
//   try {
//     const response = await axiosClient
//       .get(`/goal?groupId=${id}`)
//       .then((response) => response.data);
//     return response;
//   } catch (error) {
//     console.error(error);
//   }
// }

export async function getGroupById(id) {
  try {
    const response = await axiosClient
      .get(`/group?id=${id}`)
      .then((response) => response.data);
    return response;
  } catch (error) {
    console.error(error);
  }
}

export async function getGoalsByGroupId(id) {
  try {
    const response = await axiosClient
      .get(`/goal?groupId=${id}`)
      .then((response) => response.data);
    return response;
  } catch (error) {
    console.error(error);
  }
}

export async function getEventsByGroupId(id) {
  try {
    const response = await axiosClient
      .get(`/events?groupId=${id}`)
      .then((response) => response.data);
    return response;
  } catch (error) {
    console.error(error);
  }
}