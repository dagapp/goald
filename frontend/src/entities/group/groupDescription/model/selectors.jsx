import { createSelector } from "@reduxjs/toolkit";

const selectGroupDescriptionSelf = createSelector(
  (state) => state,
  (state) => state.groupDescription
);

export const selectGroupDescription = createSelector(
  selectGroupDescriptionSelf,
  (state) => state.groupDescription
);
export const selectGroupDescriptionLoading = createSelector(
  selectGroupDescriptionSelf,
  (state) => state.loading
);
export const selectGroupDescriptionError = createSelector(
  selectGroupDescriptionSelf,
  (state) => state.error
);
