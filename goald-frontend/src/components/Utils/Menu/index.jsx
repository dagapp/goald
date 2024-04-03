import React from 'react'

import './menu.scss'

export default function Menu({elements}) {
    return (
        <ul className='menu'>
            {elements.map(element => {
                return (
                    <li key={element.title} className="menu__element">
                        <div className="menu__element_icon">{element.icon}</div>
                        <a href="#"><div className='menu__element_title'>{element.title}</div></a>
                    </li>
                );
            })}
        </ul>
    )
}
