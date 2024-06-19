import { createSelector } from "@reduxjs/toolkit";

const selectEventsSelf = createSelector(
  (state) => state,
  (state) => state.events
);

export const selectGroupEvents = createSelector(
  selectEventsSelf,
  (state) => state.events
);
export const selectEventsLoading = createSelector(
  selectEventsSelf,
  (state) => state.loading
);
export const selectEventsError = createSelector(
  selectEventsSelf,
  (state) => state.error
);
