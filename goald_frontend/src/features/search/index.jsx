export { default as searchReducer } from "./model/searchSlice";
export { fetchSearch } from "./model/searchThunk";
export {
  selectSearchGroups,
  selectSearchError,
  selectSearchLoading,
} from "./model/selectors";

export { SearchItem } from "./ui/searchItem/searchItem";
export { Search } from "./ui/search/search";
