import { createAsyncThunk } from "@reduxjs/toolkit";
import { getGoalsByGroupId } from "@shared/api/group";

export const fetchGoals = createAsyncThunk(
  "group/goals",
  async ({ id }, thunkAPI) => {
    try {
      const response = await getGoalsByGroupId(id);
      return response;
    } catch (err) {
      return thunkAPI.rejectWithValue({
        messageError: err.message,
        status: err.response?.status,
      });
    }
  }
);
