import { useState } from "react";

import { Link } from "react-router-dom";
import { Button } from "@shared/ui/button";
import { Search } from "@features/search";

import Logo from "@shared/assets/icons/logo.svg";
import Groups from "@shared/assets/icons/groups.svg";

import { GroupList } from "@features/groupList";

import "./sidebar.scss";

export function Sidebar() {
  return (
    <div className="sidebar">
      <Link to="/">
        <div className="sidebar__header">
          <div className="sidebar__header_logo">
            <Logo />
          </div>
          <h1 className="sidebar__header_text">Goald</h1>
        </div>
      </Link>

      <div className="sidebar__menu">
        <nav className="sidebar__menu_top">
          Groups here
          {/* <GroupList /> */}
        </nav>
        <div className="sidebar__menu_bottom">User Here</div>
      </div>
    </div>
  );
}
