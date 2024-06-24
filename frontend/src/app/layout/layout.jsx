import { Sidebar } from "@widgets/sidebar";
import { Outlet } from "react-router-dom";
import "./layout.scss";

export const Layout = ({ children }) => {
  return (
    <div className="layout__wrapper">
      <Sidebar />
      <Outlet />
    </div>
  );
};
