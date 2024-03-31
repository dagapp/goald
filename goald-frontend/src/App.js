import React, {Fragment} from 'react';

import Header   from './components/Header'
import Login    from './components/Login';
import Register from './components/Register';

function App() {
    return (
        <Fragment>
            <Header />
            <Login />
        </Fragment>
    );
}

export default App;