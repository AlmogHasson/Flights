import React from 'react';
import './App.css';
import Navbar from './Components/Navbar'
import CFlights from './Components/CFlights'
import Footer from './Components/Footer'

function App() {
  return (
    <div className="App">
      <Navbar/>
      <header className="App-header">
        <CFlights/>
        <Footer/>
      </header>
    </div>
  );
}

export default App;
