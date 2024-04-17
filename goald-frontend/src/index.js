import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom'

import App from '@components/App';
import Login from '@components/Login' 
import './index.scss';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <BrowserRouter>
        <App />
        
    </BrowserRouter>
);