import { useState } from "react";

import Menu   from "@components/Utils/Menu";
import Search from "@components/Utils/Search";

// Import Icons
import standardAvatar from "@assets/user-menu/standardAvatar.svg";
import myAccountIcon from '@assets/user-menu/my-account.svg'
import logoutIcon from '@assets/user-menu/logout.svg'

import "./header.scss";

export default function Header() {
  const [open, setOpen] = useState(false);

  return (
    <header className="header">
      <Search />
      <div className="header__user">
        <div className="header__user_profile">
          <div
            className="header__user_profile-panel"
            onClick={() => setOpen(!open)}
          >
            <img
              src={standardAvatar}
              className="header__user_profile-avatar"
              alt="Standard Avatar"
            />

            <div
              className={`header__user_profile-dropdown ${
                open ? "active" : "inactive"
              }`}
            >
              <svg
                viewBox="0 0 16 9"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M8.07031 8.07129L0.999245 1.00022"
                  stroke="#ECE7F4"
                  strokeWidth="2px"
                  strokeLinecap="round"
                />
                <path
                  d="M8.07031 8.07129L15.1414 1.00022"
                  stroke="#ECE7F4"
                  strokeWidth="2px"
                  strokeLinecap="round"
                />
              </svg>
            </div>
          </div>
        </div>

        <div className={`user-menu ${open ? "active" : "inactive"}`}>
          <Menu
            elements={[
              {
                icon: myAccountIcon,
                title: "My Account",
                link: "/account",
              },
              {
                icon: logoutIcon,
                title: "Logout",
                link: "/logout",
              },
            ]}
          />
        </div>
      </div>
    </header>
  );
}
