export { default as groupDescriptionReducer } from "./model/groupDescriptionSlice";
export { fetchGroupDescription } from "./model/groupDescriptionThunk";
export {
  selectGroupDescription,
  selectGroupDescriptionError,
  selectGroupDescriptionLoading,
} from "./model/selectors";