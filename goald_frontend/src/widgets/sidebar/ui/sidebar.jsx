import { useState } from "react";

import { Link } from "react-router-dom";
import { Button } from "@shared/ui/button";
import { Search } from "@features/search";

import Logo from "@shared/assets/icons/logo.svg";
import Groups from "@shared/assets/icons/groups.svg";
import { CreateGroup } from "@features/createGroup/ui/createGroup";

import { GroupList } from "@features/groupList";

import "./sidebar.scss";

export function Sidebar() {
  const [popUpActive, setPopUpActive] = useState(false);
  const tooglePopUp = () => setPopUpActive(!popUpActive);

  return (
    <>
      <CreateGroup popUpActive={popUpActive} tooglePopUp={tooglePopUp} />
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
          <div className="sidebar__menu_top">
            <Button
              className={"sidebar__create-group-button"}
              onClick={tooglePopUp}
              Icon={Groups}
            >Create Group</Button>

            {/* <div className="sidebar__search">
            <Search />
          </div> */}

            <nav className="sidebar__menu_group-list">
              <GroupList />
            </nav>
          </div>
          <div className="sidebar__menu_bottom">User Here</div>
        </div>
      </div>
    </>
  );
}
