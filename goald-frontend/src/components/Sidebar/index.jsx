import React, { useState } from 'react'

import Menu from '@components/Utils/Menu'
import miniLogoSvg from "@assets/logo/mini-logo.svg"

import { sidebarElements } from './sidebarElements'
import './sidebar.scss'

export default function SideBar() {
    // Should be delegated to Provider or Store-Manager
    const [minimize, setMinimize] = useState(false)

    return (
        <div className={`sidebar ${minimize ? 'sidebar__mini-size' : 'sidebar__normal-size'}`}>
            <div className="sidebar__header">
                <div className="sidebar__logo">
                    <img src={miniLogoSvg} className='sidebar__logo_icon' alt="Logo"/>
                    <h1 className='sidebar__logo_text'>Goald</h1>
                </div>

                <div className="sidebar__minimize" onClick={() => setMinimize(!minimize)}>
                    <svg viewBox="0 0 16 9" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M8.07031 8.07129L0.999245 1.00022" strokeWidth="2px" strokeLinecap="round"/>
                        <path d="M8.07031 8.07129L15.1414 1.00022" strokeWidth="2px" strokeLinecap="round"/>
                    </svg>
                </div>
            </div>

            <nav className='sidebar__menu'>
                <Menu elements={sidebarElements} />
            </nav>
        </div>
    )
}