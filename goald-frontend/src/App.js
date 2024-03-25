import React, {Fragment} from 'react';

import Header  from './components/Header'
import Welcome from './components/Welcome'
import Login   from './components/Login';

function App() {
    return (
        <Fragment>
            <Header />
            <Login />
        </Fragment>
    );
}

export default App;