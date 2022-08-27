import * as React from 'react';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import Paper from '@mui/material/Paper';
import Draggable from 'react-draggable';
import InfoIcon from '@mui/icons-material/Info';



function PaperComponent(props) {
  return (
    <Draggable
      handle="#draggable-dialog-title"
      cancel={'[class*="MuiDialogContent-root"]'}
    >
      <Paper {...props} />
    </Draggable>
  );
}

export default function DraggableDialog(props) {
  const [open, setOpen] = React.useState(false);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const convertDate=(date)=>{
    var d = new Date(date);
   return d.toLocaleString();
}

  return (
    <div>
      <Button startIcon={<InfoIcon/>}  variant="contained"  onClick={handleClickOpen}>
        View more details
      </Button>

      
      <Dialog
        open={open}
        onClose={handleClose}
        PaperComponent={PaperComponent}
        aria-labelledby="draggable-dialog-title"
      >
        <DialogTitle style={{ cursor: 'move' }} id="draggable-dialog-title">
        From: {props.flight.origin_country.name} - To: {props.flight.destination_country.name}
        </DialogTitle>
        <DialogContent>
          <DialogContentText>
            Flight departing from: {props.flight.origin_country.name}<br/>
            Time of departure: {convertDate(props.flight.departure)}<br/>
            Destination country: {props.flight.destination_country.name}<br/>
            Estimated time of landing: {convertDate(props.flight.landing_time)}
            
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button autoFocus onClick={handleClose}>
            Cancel
          </Button>
          <Button onClick={handleClose}>Subscribe</Button>
        </DialogActions>
      </Dialog>
    </div>
  );
}
