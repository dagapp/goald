import React from 'react'

import standardAvatar from "../../assets/icons/user/standardAvatar.svg"
import arrowDown from "../../assets/icons/utils/arrow.svg"

import './header.scss'

export default function Header() {
    return (
        <header className='header'>
            <div className='header__user'>
                <img src={standardAvatar} className='header__user_avatar' alt="Standard Avatar"/>
                {/* <div className="header__user_nickname">Roman Abramov</div> */}
                <img src={arrowDown} className='header__user_dropdown' alt="Arrow Down" />
            </div>
        </header>
    )
}