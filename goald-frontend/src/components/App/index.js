import {Routes, Route} from 'react-router-dom'

//Layout
import Header from "@components/Header";
import SideBar from "@components/Sidebar";

// Pages
import Login     from "@components/Login";
import Register  from "@components/Register";
import Group     from "@components/Group";
import GroupList from "@components/GroupList";
import Account   from "@components/Account";

import "./app.scss";

export default function App() {
  return (
    <div className="app">
      <SideBar />
      <div className="app-content">
        <Header />
        <Routes>
          <Route path="/account" element={<Account  />} />
          <Route path="/group"   element={<Group    />} />
          <Route path="/groups"  element={<GroupList/>} />
        </Routes>
      </div>
    </div>
  );
}
