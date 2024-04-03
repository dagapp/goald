import React from 'react'

import Menu   from '../Utils/Menu'
import Search from '../Utils/Search'

import logoSvg from "../../assets/logo/logo.svg"
import miniLogoSvg from "../../assets/logo/mini-logo.svg"

import { sidebarElements } from './sidebarElements'
import './sidebar.scss'

export default function SideBar() {
    return (
        <div className="sidebar">
            <div className="sidebar__logo">
                <img src={miniLogoSvg} className='sidebar__logo_icon' alt="Logo"/>
                <img src={logoSvg} className='sidebar__logo_text' alt="GOALD"/>
            </div>

            <nav className='sidebar__menu'>
                <Search />
                <Menu elements={sidebarElements} />
            </nav>
        </div>
    )
}
