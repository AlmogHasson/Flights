import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
// import axios from 'axios';
import {getFlights} from './flightAPI'


// the initial props of the slice
const initialState = {
  status: 'idle',
  flightArr: [], //value,
  // URL: 'http://127.0.0.1:8000/',
};

// ------------------------------------------  -GET-  ------------------------------------------
// call the method in the API
const fetchAllFlights = createAsyncThunk(
  'flight/getFlights',
  async () => {
    const response = await getFlights();
    // console.log(response.data)
    return response.data;
  }
);
// creating an async function that grabs the token from the local storage and returns the data
// const fetchAllFlights = createAsyncThunk(
//   'flight/getFlights', async () => {
//     const response = await axios.get(
//       `${initialState.URL}flights`,
//       // { headers: { 'Authorization': `Bearer ${localStorage.getItem('tokens')}` } }//might not grant token if not logged
//     );
//     console.log(response.data)
//     return response.data;
//   })

export const flightSlice = createSlice({
  name: 'flight',
  initialState,
  extraReducers: builder => {
    //pending - loading
    builder.addCase(fetchAllFlights.pending, state => {
      state.status = 'loading'
      
    })
    // success - load the data into the flights arr
    builder.addCase(fetchAllFlights.fulfilled, (state, action) => {
      state.status = 'success'
      state.flightArr = action.payload
      state.error = ''
      // console.log(state.flightArr)
    })
    // rejected - get error message
    builder.addCase(fetchAllFlights.rejected, (state, action) => {
      state.status = 'idle'
      state.flightArr = []
    })
  }
})


export { fetchAllFlights }
export const showAllFlights = (state) => state.flight.flightArr //variable that access the data in the slice
export default flightSlice.reducer