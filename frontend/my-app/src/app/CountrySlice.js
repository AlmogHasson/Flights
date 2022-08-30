import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import {getCountries} from './CountryAPI'


// the initial props of the slice
const initialState = {
  status: 'idle',
  countryArr: [], 
};
// --------------------------------------------------------------------  -GET-  ---------------------------------------------------
// call the method in the API
const fetchAllCountries = createAsyncThunk(
  'country/getCountries',
  async () => {
    const response = await getCountries();
    let countries = response.data
    // { code: 'AD', label: 'Andorra', phone: '376' },
    console.log(response.data)
    countries = countries.map(item => {
      return {
          label: item.name,
          // code: item.id
      }
  })
    return countries;
  }
);

// export const getCountryAsync = createAsyncThunk(
//   'country/getCountry',
//   async () => {
//     const response = await getCountry();
//     let countries = response.data
//     countries = countries.map(item => {
//       return {
//           label: item.country_name,
//           value: item.id
//       }
//   })
//     return countries;
//   }
// );

export const countrySlice = createSlice({
  name: 'country',
  initialState,
  extraReducers: builder => {
    //pending - loading
    builder.addCase(fetchAllCountries.pending, state => {
      state.status = 'loading'
      
    })
    // success - load the data into the countrys arr
    builder.addCase(fetchAllCountries.fulfilled, (state, action) => {
      state.status = 'success'
      state.countryArr = action.payload
      state.error = ''
      // console.log(state.countryArr)
    })
    // rejected - get error message
    builder.addCase(fetchAllCountries.rejected, (state, action) => {
      state.status = 'idle'
      state.countryArr = []
    })
  }
})


export { fetchAllCountries }
export const showAllCountries = (state) => state.country.countryArr //variable that access the data in the slice
export default countrySlice.reducer