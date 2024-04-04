import React from 'react';

import Header   from '@components/Header'
import Login    from '@components/Login';
import Register from '@components/Register';

import SideBar  from '@components/Sidebar';
import Feed     from '@components/Feed'

import './app.scss'

export default function App() {
    return (
        <div className='app'>
            <SideBar />  
            <Header />
        </div>
    );
}