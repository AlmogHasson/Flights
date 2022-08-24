// import { Card } from '@mui/material';
import React from 'react';
import './App.css';
// import CFlights from './Components/CFlights';
import Navbar from './Components/Navbar'
// import Card from './Components/Card'
import CFlights from './Components/CFlights'

function App() {
  return (
    <div className="App">
      <Navbar/>
      <br />
      <br />
      <CFlights/>
      <header className="App-header">
        {/* <Card/> */}
        
      </header>

    </div>
  );
}

export default App;
