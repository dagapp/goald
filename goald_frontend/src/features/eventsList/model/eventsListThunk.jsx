import { createAsyncThunk } from "@reduxjs/toolkit";
import { getEventsByGroupId } from "@shared/api/group";

export const fetchEvents = createAsyncThunk(
  "group/events",
  async ({ id }, thunkAPI) => {
    try {
      const response = await getEventsByGroupId(id);
      return response;
    } catch (err) {
      return thunkAPI.rejectWithValue({
        messageError: err.message,
        status: err.response?.status,
      });
    }
  }
);
