import { useState } from "react";

import { Button } from "@shared/ui/button";
import { Search } from "@features/search";

import Logo from "@shared/assets/icons/logo.svg";
import Analytics from "@shared/assets/icons/analytics.svg";
import Groups from "@shared/assets/icons/groups.svg";

import { getGroupById, getGoalsByGroupId } from "@shared/api/group";

import "./sidebar.scss";

function SidebarExtension(props) {
  const { title, innerComponent } = props;

  return (
    <div className="sidebar-extension">
      <div className="sidebar-extension__title">{title}</div>
      {innerComponent}
    </div>
  );
}

export function Sidebar() {
  const [extensionTitle, setExtensionTitle] = useState("");
  const [innerComponent, setInnerComponent] = useState();

  const renderAnalytics = () => {
    setExtensionTitle("Analytics");

    // Move to the features
    // setInnerComponent(
    //   <div className="test">
    //     <Button Icon={Analytics} className={"sidebar__menu__button"}>
    //       Lorem Ipsum
    //     </Button>
    //     <Button Icon={Analytics} className={"sidebar__menu__button"}>
    //       Lorem Ipsum Ipsum
    //     </Button>
    //   </div>
    // );
  };

  const renderGroups = () => {
    setExtensionTitle("My Groups");
    setInnerComponent(<Search />);
  };

  return (
    <div className="sidebar-wrapper">
      <div className="sidebar">
        <div className="sidebar__logo">
          <Logo />
        </div>
        <nav className="sidebar__menu">
          {/* <Button
            Icon={Analytics}
            className={"sidebar__menu__button"}
            onClick={renderAnalytics}
          /> */}
          <Button
            Icon={Groups}
            className={"sidebar__menu__button"}
            onClick={renderGroups}
          />
        </nav>
      </div>
      {extensionTitle && (
        <SidebarExtension
          title={extensionTitle}
          innerComponent={innerComponent}
        />
      )}
    </div>
  );
}
