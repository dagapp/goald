export { default as eventsReducer } from "./model/eventsListSlice";
export { fetchEvents } from "./model/eventsListThunk";
export {
  selectGroupEvents,
  selectEventsError,
  selectEventsLoading,
} from "./model/selectors";

export { EventsList } from "./ui/eventsList";