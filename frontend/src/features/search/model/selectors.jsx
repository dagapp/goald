import { createSelector } from "@reduxjs/toolkit";

const selectSearchSelf = createSelector(
  (state) => state,
  (state) => state.search
);

export const selectSearchGroups = createSelector(
  selectSearchSelf,
  (state) => state.groups
);
export const selectSearchLoading = createSelector(
  selectSearchSelf,
  (state) => state.loading
);
export const selectSearchError = createSelector(
  selectSearchSelf,
  (state) => state.error
);
