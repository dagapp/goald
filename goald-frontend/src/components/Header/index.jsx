import React from 'react'

import logoSvg from "../../assets/logo.svg"
import themeSwitchDark from "../../assets/icons/mode/theme-switch-dark.svg"
import themeSwitchLight from "../../assets/icons/mode/theme-switch-light.svg"

import './header.scss'

export default function Header() {
  return (
    <header>
        <div className="header__container">
            <div className="header__logo">
                <a href="#" className="header__logo"><img src={logoSvg} alt="GOALD"/></a>
            </div>
            
            <div className="header__theme">
                <img src={themeSwitchDark} alt="Dark"></img>
            </div>
        </div>
    </header>
  )
}