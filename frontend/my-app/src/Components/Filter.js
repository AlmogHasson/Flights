import * as React from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import {showAllCountries, fetchAllCountries } from '../app/CountrySlice';
import { useSelector, useDispatch } from 'react-redux';
import { useEffect } from 'react';

  // return (
  //     <div className="test">
  //         {countries.map((country) => (
  //             <div className="country" key={country.id}>
  //                 {country.name }
  //             </div>
              
  //         ))}

  //     </div>

  // );
  
export default function CountrySelect() {
  
  const countries = useSelector(showAllCountries)
  const dispatch = useDispatch();
  // const data = new FormData(event.currentTarget);

  useEffect(() => {
      dispatch(fetchAllCountries())
  }, [])



  return (
    <Autocomplete
      id="country-select-demo"
      sx={{ width: 300 }}
      options={countries}
      autoHighlight
      getOptionLabel={(option) => option.label}
      renderOption={(props, option) => (
        <Box component="li" sx={{ '& > img': { mr: 2, flexShrink: 0 } }} {...props}>
          <img
            loading="lazy"
            width="20"
            // src={`https://flagcdn.com/w20/${option.code.toLowerCase()}.png`}
            // srcSet={`https://flagcdn.com/w40/${option.code.toLowerCase()}.png 2x`}
            alt=""
          />
          {option.label}
        </Box>
      )}
      renderInput={(params) => (
        <TextField
          {...params}
          label="Choose a country"
          inputProps={{
            ...params.inputProps,
            autoComplete: 'new-password', // disable autocomplete and autofill
          }}
        />
      )}
    />
  );
}

