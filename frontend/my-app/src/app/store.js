import { configureStore } from '@reduxjs/toolkit';
import countrySlice from './CountrySlice';
import  flightSlice  from './flightSlice';


export const store = configureStore({
  reducer: {
    flight: flightSlice,
    country: countrySlice,
  },
});
