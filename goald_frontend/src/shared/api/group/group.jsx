import { axiosClient } from "@shared/api/axiosClient";

export async function getUserGroups() {
  try {
    const response = await axiosClient
      .get('/group')
      .then((response) => response.data);
    return response;
  } catch (error) {
    console.error(error);
  }
}

export async function getGroupDescriptionById(id) {
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

export async function createGoal(name) {
  try {
    const response = await axiosClient
      .post(`/goal`, { name: name })
      .then((response) => response.data);
    return response;
  } catch (error) {
    console.error(error);
  }
}
