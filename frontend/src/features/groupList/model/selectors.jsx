import { createSelector } from "@reduxjs/toolkit";

const selectGroupListSelf = createSelector(
  (state) => state,
  (state) => state.groupList
);

export const selectGroupList = createSelector(
  selectGroupListSelf,
  (state) => state.groupList
);
export const selectGroupListLoading = createSelector(
  selectGroupListSelf,
  (state) => state.loading
);
export const selectGroupListError = createSelector(
  selectGroupListSelf,
  (state) => state.error
);
