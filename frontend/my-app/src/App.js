import React from 'react';
import './App.css';
import Navbar from './Components/Navbar'
import CFlights from './Components/CFlights'
import CTickets from './Components/CTickets'
import Login from './Components/Login'
import Footer from './Components/Footer'
import { Routes, Route } from 'react-router-dom';
import Register from './Components/Register'
import Countries from './Components/Countries';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Navbar />
        <Routes>
          <Route path='/' element={<CFlights />} />
          <Route path='/flights' element={<CFlights />} />
          <Route path='/tickets' element={<CTickets />} />
          <Route path='/register' element={<Register />} />
          <Route path='/login' element={<Login />} />
        </Routes>
        <Footer />
      </header>
    </div>
  );
}

export default App;
