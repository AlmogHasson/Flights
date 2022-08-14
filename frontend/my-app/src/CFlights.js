import { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchAllFlights, showAllFlights } from './app/flightSlice';

// here all the html like things happen

const CFlights = () => {
    const dispatch = useDispatch();
    const flights = useSelector(showAllFlights);

    useEffect(() => {
        dispatch(fetchAllFlights())
    },[])

    return (
        <div >
            <p>test</p>
            {flights && flights.map((flight)=>
            <div key={flight.id}>
            {flight.id}{" | "}
            {flight.destination_country}{" | "}
            {flight.origin_country}{" | "}
            {flight.airline_company}{" | "}
            {flight.departure}{" | "}
            {flight.landing_time}{" | "}
            </div>)}
            {/* {console.log(flights)} */}
        </div>
    )
}


export default CFlights