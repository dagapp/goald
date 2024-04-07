import React from 'react'

import './menu.scss'

export default function Menu({elements}) {
    return (
        <ul className='menu'>
            {elements.map(element => {
                return (
                    <li key={element.title}>
                        <a href="#" className="menu__element">
                            <img src={element.icon} className='menu__element_icon' />
                            <div className='menu__element_title'>{element.title}</div>
                        </a>
                    </li>
                );
            })}
        </ul>
    )
}
