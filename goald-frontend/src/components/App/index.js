import React from "react";

import Header from "@components/Header";
import Login from "@components/Login";
import Register from "@components/Register";
import Group from "@components/Group";

import SideBar from "@components/Sidebar";

import Info from "@components/Group/Widgets/Info";
import "./app.scss";

export default function App() {
  return (
    <div className="app">
      <SideBar />
      <div className="app-content">
        <Header />
        <Group />
      </div>
    </div>
  );
}
