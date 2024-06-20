import { createSelector } from "@reduxjs/toolkit";

const selectGoalsSelf = createSelector(
  (state) => state,
  (state) => state.goals
);

export const selectGroupGoals = createSelector(
  selectGoalsSelf,
  (state) => state.goals
);
export const selectGoalsLoading = createSelector(
  selectGoalsSelf,
  (state) => state.loading
);
export const selectGoalsError = createSelector(
  selectGoalsSelf,
  (state) => state.error
);
