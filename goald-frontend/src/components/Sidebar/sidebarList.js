import React from 'react'

export default function SidebarList({elements, description=""}) {
    return (
        <ul className='sidebar__list'>
            {/* <div className='sidebar__list_description'>{description}</div> */}
            {elements.map(element => { 
                return (
                    <li key={element.title} className="sidebar__element">
                        <div className="sidebar__element_icon">{element.icon}</div>
                        {/* <div className='sidebar__element_indicator'></div> */}
                        <a href="#"><div className='sidebar__element_title'>{element.title}</div></a>
                    </li>
                );
            })}
            {/* <hr className='sidebar__list_divider' /> */}
        </ul>
    )
}
