import * as React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { useSelector, useDispatch } from 'react-redux';
import { fetchAllFlights, showAllFlights } from '../app/flightSlice';
import { useEffect } from 'react';

export default function ImgMediaCard() {
    const flights = useSelector(showAllFlights)
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(fetchAllFlights())
    }, [])

    return (
        <div>
            {/* <Grid> */}
                {flights && flights.map((flight) =>
                <div key={flight.id}>
                    <Card sx={{ maxWidth: 345 }}>
                        <CardMedia
                            component="img"
                            alt="japan"
                            height="140"
                            image=""
                        />
                        <CardContent>
                            <Typography gutterBottom variant="h5" component="div">
                            From: {flight.origin_country.name}<br/>
                            To:{flight.destination_country.name}<br/>
                            Flight company: {flight.airline_company.name}
                            </Typography>
                            <Typography variant="body2" color="text.secondary">
                                Departure on :   {flight.departure}
                                EST landing time:  {flight.landing_time}
                            </Typography>
                        </CardContent>
                        <CardActions>
                            <Button size="small">Share</Button>
                            <Button size="small">Learn More</Button>
                        </CardActions>
                    </Card>
                </div>)}
            {/* </Grid> */}
            


        </div>
    );
}
