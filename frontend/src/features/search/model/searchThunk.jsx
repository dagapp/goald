import { createAsyncThunk } from "@reduxjs/toolkit";
import { getResultSearch } from "@shared/api/search";

export const fetchSearch = createAsyncThunk(
  "groups/fetchSearch",
  async ({ searchString }, thunkAPI) => {
    try {
      const response = await getResultSearch(searchString);
      return response;
    } catch (err) {
      return thunkAPI.rejectWithValue({
        messageError: err.message,
        status: err.response?.status,
      });
    }
  }
);
