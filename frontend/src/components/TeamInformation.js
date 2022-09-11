import React, {useState}  from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Collapse from '@mui/material/Collapse';
import Stack from "@mui/material/Stack"
import axios from "axios";
import { Link } from "react-router-dom";

const baseURL = "http://127.0.0.1:5000/start_game";

export default function TeamInformation() {
  const [post, setPost] = React.useState(null);
  const [open, setOpen] = useState(false);
  const [value, setValue] = React.useState('Controlled');

  const handleChange = (event) => {
    console.log(value)
    setValue(event.target.value);
  };

  function startGame() {
    const headers = {
      'Content-Type': 'application/json'
    }
    axios.post(baseURL, {
        team_information: value
      }, 
      {
        headers: headers
      })
      .then((response) => {
        setPost(response.data);
        console.log(post);
      });
  }

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
            onChange={handleChange}
            multiline
            fullWidth
          />

      </Box>
      <Box
        sx={{px:4, width:"80%"}}> 
        <Stack direction="row" justifyContent="space-between">
          <Button  color="primary"onClick={() => setOpen(state => !open)}> Guide Me</Button>
          <Link to={"/enter_result"}><Button  variant="contained" onClick={startGame}>Enter</Button></Link>
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
