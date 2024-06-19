import { createAsyncThunk } from "@reduxjs/toolkit";
import { getGroupDescriptionById } from "@shared/api/group";

export const fetchGroupDescription = createAsyncThunk(
  "group/groupDescription",
  async ({ id }, thunkAPI) => {
    try {
      const response = await getGroupDescriptionById(id);
      return response;
    } catch (err) {
      return thunkAPI.rejectWithValue({
        messageError: err.message,
        status: err.response?.status,
      });
    }
  }
);
