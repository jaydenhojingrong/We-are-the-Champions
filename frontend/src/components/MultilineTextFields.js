import React, {useState}  from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Collapse from '@mui/material/Collapse';
import Stack from "@mui/material/Stack"

export default function MultilineTextFields() {
  // const [value, setValue] = useState('Controlled');
  const [open, setOpen] = useState(false);

  // const handleChange = (event) => {
  //   setValue(event.target.value);
  // };

  return (
    <Box>
      <Box
        sx={{p:4, width:"80%"}}
        display="flex"
        justifyContent="center"
        alignItems="center"> 

        <TextField
            id="outlined-textarea"
            label="Enter Team Information Here"
            placeholder="e.g. 
  teamA 01/04 1
  teamB 04/04 2"
            minRows={12}
            multiline
            fullWidth
          />

      </Box>
      <Box
        sx={{px:4, width:"80%"}}> 
        <Stack direction="row" spacing={2}>
          <Button  color="primary"onClick={() => setOpen(state => !open)}> Guide Me</Button>
          <Button justifyContent="flex-end" variant="contained">Enter</Button>
        </Stack>
        <Collapse in={open}>
            <ul>
              <li>Team format must be "Team_name Date_registered(MM/YY) Group_name"</li>
              <li>Each team is entered in a single line</li>
              <li>Enter information for only 12 teams</li>
              <li>Only two different groups should exist</li>
              <li>Each group contains 6 teams only</li>
            </ul>
          </Collapse>
      </Box>
      
    </Box>
  );
}
