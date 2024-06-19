export { default as goalsReducer } from "./model/goalsListSlice";
export { fetchGoals } from "./model/goalsListThunk";
export {
  selectGroupGoals,
  selectGoalsError,
  selectGoalsLoading,
} from "./model/selectors";

export { GoalsList } from "./ui/goalsList";