import { useState } from "react";
import { Link, Navigate } from "react-router-dom";
import { useDispatch } from "react-redux";

import { Button } from "@shared/ui/button";
import { Search } from "@features/search";

import { logout } from "@entities/user/model/authSlice";

import Logo from "@shared/assets/icons/logo.svg";
import Groups from "@shared/assets/icons/groups.svg";
import { CreateGroup } from "@features/createGroup/ui/createGroup";

import { GroupList } from "@features/groupList";

import "./sidebar.scss";

export function Sidebar() {
  const [popUpActive, setPopUpActive] = useState(false);
  const tooglePopUp = () => setPopUpActive(!popUpActive);
  
  const dispatch = useDispatch();

  const onClickLogout = () => {
    dispatch(logout());
    <Navigate to="/login" />
  }

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
            >
              Create Group
            </Button>

            {/* <div className="sidebar__search">
            <Search />
          </div> */}

            <nav className="sidebar__menu_group-list">
              <GroupList />
            </nav>
          </div>
          <div className="sidebar__menu_bottom">
            <Button
              className="sidebar__menu_bottom_logout-button"
              onClick={() => onClickLogout()}
            >
              Logout
            </Button>
          </div>
        </div>
      </div>
    </>
  );
}
