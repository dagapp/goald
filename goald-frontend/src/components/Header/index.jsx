import React from 'react'

import logoSvg from "../../assets/logo.svg"
import './header.scss'

export default function Header() {
  return (
    <header>
        <div className="header__container">
            <a href="" className="header__logo"><img src={logoSvg} alt="GOALD"/></a>
            <div className="header__navigation">
                {/* <nav className="menu">
                    <ul className="menu__body">
                        <li className="menu__item"><a href="#" className="menu__link">Features</a></li>
                        <li className="menu__item"><a href="#" className="menu__link">FAQ</a></li>
                        <li className="menu__item"><a href="#" className="menu__link">About Us</a></li>
                    </ul>
                </nav> */}
                <div className="header__buttons">
                    <button className="header__button">Войти</button>
                    <button className="header__button gradient__button">Регистрация</button>
                </div>
            </div>
        </div>
    </header>
  )
}