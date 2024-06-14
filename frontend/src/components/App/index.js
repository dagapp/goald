import { Routes, Route } from "react-router-dom";

//Layout
import Header from "@components/Header";
import SideBar from "@components/Sidebar";

// Pages
import Login from "@components/Login";
import Register from "@components/Register";
import Group from "@components/Group";
import GroupList from "@components/GroupList";
import Account from "@components/Account";

import "./app.scss";

function Wrapper(component) {
  console.log(component);
  return (
    <div className="app">
      <SideBar />
      <div className="app-content">
        <Header />
        <div>{component}</div>
      </div>
    </div>
  );
}

export default function App() {
  return (
    <div>
    <Routes>
      <Route path="/" element={Wrapper(<Account />)} />
      <Route path="/account" element={Wrapper(<Account />)} />
      <Route path="/group" element={Wrapper(<Group />)} />
      <Route path="/groups" element={Wrapper(<GroupList />)} />

      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
    </Routes>
    </div>
  );
}
