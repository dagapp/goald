import ReactDOM from 'react-dom/client';
import { BrowserRouter, Route, Routes } from 'react-router-dom'

import App       from '@components/App';

// Pages
import Login     from "@components/Login";
import Register  from "@components/Register";

import Group     from "@components/Group";
import GroupList from "@components/GroupList";
import Account   from "@components/Account";

import './index.scss';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <BrowserRouter>  
        <App/>
    </BrowserRouter>
);