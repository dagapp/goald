import { createSlice } from "@reduxjs/toolkit";
import { fetchGroupList } from "./groupListThunk";

const initialState = { groupList: null, loading: false, error: null };

const groupListSlice = createSlice({
  name: "groupList",
  initialState,
  reducers: {},
  extraReducers: (builder) =>
    builder
      .addCase(fetchGroupList.pending, (state) => {
        state.loading = true;
      })
      .addCase(fetchGroupList.fulfilled, (state, action) => {
        state.groupList = action.payload;
        state.loading = false;
        state.error = null;
      })
      .addCase(fetchGroupList.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload ?? null;
      }),
});

export default groupListSlice.reducer;
