import { createSelector } from "@reduxjs/toolkit";

const selectAuthSelf = createSelector(
  (state) => state,
  (state) => state.data
);

export const selectAuth = createSelector(
  selectAuthSelf,
  (state) => state.data
);
export const selectAuthLoading = createSelector(
  selectAuthSelf,
  (state) => state.loading
);
export const selectAuthError = createSelector(
  selectAuthSelf,
  (state) => state.error
);
