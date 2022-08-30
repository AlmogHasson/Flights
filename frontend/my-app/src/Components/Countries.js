import * as React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useEffect } from 'react';
import { fetchAllCountries, showAllCountries } from '../app/CountrySlice';

export default function Countries() {
    const countries = useSelector(showAllCountries)
    const dispatch = useDispatch();


    useEffect(() => {
        dispatch(fetchAllCountries())
    }, [])

    return (
        <div className="test">
            hello
            {countries.map((country) => (
                <div className="country">
                    {country.name }
                </div>
                
            ))}

        </div>

    );
}