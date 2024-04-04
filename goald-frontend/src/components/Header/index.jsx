import React, { useState } from 'react'

import Menu from '@components/Utils/Menu'

import standardAvatar from "@assets/icons/user/standardAvatar.svg"
import arrowDown from "@assets/icons/utils/arrow.svg"

import { userOptions } from './userOptions'
import './header.scss'

export default function Header() {
    const [open, setOpen] = useState(false)

    return (
        <header className='header'>
            <div className='header__user'>
                <div className="header__user_profile">
                    <div className="header__user_profile-panel" onClick={() => setOpen(!open)}>
                        <img src={standardAvatar} className='header__user_profile-avatar' alt="Standard Avatar"/>
                        <div className={`header__user_profile-dropdown ${open ? 'active' : 'inactive'}`}>
                            <img src={arrowDown} alt="Arrow Down" />
                        </div>
                    </div>
                </div>
                
                <div className={`user-menu ${open ? 'active' : 'inactive'}`}>
                    <Menu elements={userOptions} />
                </div> 
            </div>
        </header>
    )
}