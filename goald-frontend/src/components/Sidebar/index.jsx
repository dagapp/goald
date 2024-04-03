import React from 'react'

import { sidebarElements } from './sidebarElements'
import SidebarList from './sidebarList'

import logoSvg from "../../assets/logo/logo.svg"
import miniLogoSvg from "../../assets/logo/mini-logo.svg"

import './sidebar.scss'

export default function SideBar() {
    return (
        <div className="sidebar">
            <div className="sidebar__logo">
                <img src={miniLogoSvg} className='sidebar__logo_icon' alt="LOGO"/>
                <img src={logoSvg} className='sidebar__logo_text' alt="GOALD"/>
            </div>

            <nav>
                <div className="sidebar__search">
                    <svg focusable="false" className="sidebar__search_icon" alt="Magnifier" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                        <path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"></path>
                    </svg>
                    <input type="text" className="sidebar__search_input" placeholder='Search Groups or Users'/>
                </div>
                <SidebarList elements={sidebarElements} description='Main'/>
            </nav>
        </div>
    )
}
