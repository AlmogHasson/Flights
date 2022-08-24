import * as React from 'react';
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { useSelector, useDispatch } from 'react-redux';
import { fetchAllFlights, showAllFlights } from '../app/flightSlice';
import { useEffect } from 'react';
import DraggableDialog from './DraggableDialog';


// image== name> according to location, display image according to flight

const theme = createTheme();

export default function FlightAlbum() {
    const flights = useSelector(showAllFlights)
    const dispatch = useDispatch();
    

    useEffect(() => {
        dispatch(fetchAllFlights())
    }, [])

    const convertDate=(date)=>{
        var d = new Date(date);
       return d.toLocaleString();
    }

    return (
        <ThemeProvider theme={theme}>
            <main>
                <Container sx={{ py: 8 }} maxWidth="md">
                    {/* End hero unit */}
                    <Grid container spacing={5}>
                        {flights.map((flight) => (
                            <Grid item key={flight} xs={5} sm={6} md={4}>
                                <Card sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
                                    <CardMedia
                                        sx={{
                                            // 16:9
                                            pt: '56.25%',
                                        }}
                                        image="./japan.jpg"
                                        alt="random"
                                    />
                                    <CardContent sx={{ flexGrow: 1 }}>
                                        <Typography gutterBottom variant="h5" component="h2">
                                            {flight.airline_company.name}
                                        </Typography>
                                        <Typography>
                                            From: {flight.origin_country.name} Departure: {convertDate(flight.departure)} <br />
                                            To: {flight.destination_country.name} Landing Time: {convertDate(flight.landing_time)}
                                        </Typography>
                                    </CardContent>
                                    <CardActions>
                                        <DraggableDialog flight={flight}></DraggableDialog>
                                        <Button size="small">View More Details</Button>
                                    </CardActions>
                                </Card>
                            </Grid>
                        ))}
                    </Grid>
                </Container>
            </main>
        </ThemeProvider>
    );
}