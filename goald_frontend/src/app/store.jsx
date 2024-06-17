import { combineReducers, configureStore } from "@reduxjs/toolkit";

import { searchReducer } from "@features/search";
import { groupDescriptionReducer } from "@entities/group/groupDescription";
import { groupListReducer } from "@features/groupList";
import { goalsReducer } from "@features/goals/goalsList";
import { eventsReducer } from "@features/eventsList";

const rootReducer = combineReducers({
  search: searchReducer,
  goals: goalsReducer,
  events: eventsReducer,
  groupDescription: groupDescriptionReducer,
  groupList: groupListReducer,
});

const store = configureStore({
  reducer: rootReducer,
});

export default store;
