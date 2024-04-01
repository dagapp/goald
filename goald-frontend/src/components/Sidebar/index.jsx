import React from 'react'

import { sidebarElements } from './sidebarElements'

import logoSvg from "../../assets/logo.svg"
import './sidebar.scss'

export default function SideBar() {
    return (
        <div className="sidebar">
            <div className="sidebar__logo">
                <img src={logoSvg} alt="GOALD"/>
            </div>

            <nav>
                <ul className='sidebar__list'>
                    {sidebarElements.map(element => { 
                        return (
                            <li key={element.title} className="sidebar__element">
                                <img src={element.icon} className="sidebar__element_icon" alt={element.title}/>

                                <a href="#" className="">
                                    <div className='sidebar__element_title'>{element.title}</div>
                                </a>
                            </li>
                        );
                    })}
                </ul>
            </nav>
        </div>
    )

}
