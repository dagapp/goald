import { Provider } from "react-redux";
import store from "@app/store";

export const Providers = ({ children }) => {
  return <Provider store={store}>{children} </Provider>;
};
