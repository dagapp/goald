import { axiosClient } from "@shared/api/axiosClient";

export async function getUserGroups() {
  try {
    const response = await axiosClient
      .get("/group/", { withCredentials: true })
      .then((response) => response.data.results);
    return response;
  } catch (error) {
    console.error(error);
  }
}

export async function getGroupDescriptionById(id) {
  try {
    const response = await axiosClient
      .get(`/group/${id}/`, { withCredentials: true })
      .then((response) => response.data);
    return response;
  } catch (error) {
    console.error(error);
  }
}

export async function getGoalsByGroupId(id) {
  try {
    const response = await axiosClient
      .get(`/group/${id}/goals/`, { withCredentials: true })
      .then((response) => response.data);
    return response;
  } catch (error) {
    console.error(error);
  }
}

export async function getEventsByGroupId(id) {
  try {
    const response = await axiosClient
      .get(`/group/${id}/events/`, { withCredentials: true })
      .then((response) => response.data);
    return response;
  } catch (error) {
    console.error(error);
  }
}

export async function createGroup(params) {
  try {
    const { name, tag } = params;
    const response = await axiosClient
      .post(`/group/`, { name: name, tag: tag }, { withCredentials: true })
      .then((response) => response.data);
    return response;
  } catch (error) {
    console.error(error);
  }
}

export async function createGoal(params) {
  try {
    const { name, group, is_active, final_value } = params;
    const response = await axiosClient
      .post(
        `/goal/`,
        {
          name: name,
          group: group,
          is_active: is_active,
          final_value: final_value,
        },
        { withCredentials: true }
      )
      .then((response) => response.data);
    return response;
  } catch (error) {
    console.error(error);
  }
}
