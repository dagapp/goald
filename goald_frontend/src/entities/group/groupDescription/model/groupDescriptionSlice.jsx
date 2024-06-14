import { createSlice } from "@reduxjs/toolkit";
import { fetchGroupDescription } from "./groupDescriptionThunk";

const initialState = { groupDescription: null, loading: false, error: null };

const groupDescriptionSlice = createSlice({
  name: "groupDescription",
  initialState,
  reducers: {},
  extraReducers: (builder) =>
    builder
      .addCase(fetchGroupDescription.pending, (state) => {
        state.loading = true;
      })
      .addCase(fetchGroupDescription.fulfilled, (state, action) => {
        state.groupDescription = action.payload[0].name
        state.loading = false;
        state.error = null;
      })
      .addCase(fetchGroupDescription.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload ?? null;
      }),
});

export default groupDescriptionSlice.reducer;
