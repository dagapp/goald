import { Link } from 'react-router-dom';
import './menu.scss'

export default function Menu({elements}) {
    return (
        <ul className='menu'>
            {elements.map((element,index) => {
                return (
                    <li key={index}>
                        <Link to={element.link} className="menu__element">
                            <img src={element.icon} className='menu__element_icon' />
                            <div className='menu__element_title'>{element.title}</div>
                        </Link>
                    </li>
                );
            })}
        </ul>
    )
}
