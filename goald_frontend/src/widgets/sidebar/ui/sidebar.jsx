import { Button } from "@shared/ui/button";
import { Search } from "@features/search";

import Logo from "@shared/assets/icons/logo.svg";
import Groups from "@shared/assets/icons/groups.svg";

import "./sidebar.scss";

export function Sidebar() {
  return (
    <div className="sidebar-wrapper">
      <div className="sidebar">
        <div className="sidebar__logo">
          <Logo />
        </div>
        <nav className="sidebar__menu">
          <Button
            Icon={Groups}
            className={"sidebar__menu__button"}
            onClick={() => {}}
          />
        </nav>
      </div>
      <div className="sidebar-extension">
        <Search />
      </div>
    </div>
  );
}
