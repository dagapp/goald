import { combineReducers, configureStore } from "@reduxjs/toolkit";

import { searchReducer } from "@features/search";
import { groupDescriptionReducer } from "@entities/group/groupDescription";
import { groupListReducer } from "@features/groupList";
import { goalsReducer } from "@features/goals/goalsList";
import { eventsReducer } from "@features/eventsList";
import { authReducer } from "@entities/user";

const rootReducer = combineReducers({
  search: searchReducer,
  goals: goalsReducer,
  events: eventsReducer,
  groupDescription: groupDescriptionReducer,
  groupList: groupListReducer,
  auth: authReducer,
});

const store = configureStore({
  reducer: rootReducer,
});

export default store;
