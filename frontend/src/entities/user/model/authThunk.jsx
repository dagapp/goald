import { createAsyncThunk } from "@reduxjs/toolkit";
import { authLogin } from "@shared/api/auth";

export const fetchAuth = createAsyncThunk(
  "auth",
  async (params, thunkAPI) => {
    try {
      const response = await authLogin(params);
      return response;
    } catch (err) {
      return thunkAPI.rejectWithValue({
        messageError: err.message,
        status: err.response?.status,
      });
    }
  }
);
