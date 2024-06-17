import { createAsyncThunk } from "@reduxjs/toolkit";
import { getUserGroups } from "@shared/api/group";

export const fetchGroupList = createAsyncThunk(
  "group/groupList",
  async ({}, thunkAPI) => {
    try {
      const response = await getUserGroups();
      return response;
    } catch (err) {
      return thunkAPI.rejectWithValue({
        messageError: err.message,
        status: err.response?.status,
      });
    }
  }
);
