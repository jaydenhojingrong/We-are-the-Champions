import React, {useState}  from 'react';
import Box from '@mui/material/Box';
import axios from "axios";
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Collapse from '@mui/material/Collapse';
import Stack from "@mui/material/Stack"
import { Link } from "react-router-dom";
import CircleOutlinedIcon from '@mui/icons-material/CircleOutlined';
import CircleIcon from '@mui/icons-material/Circle';

// const baseURL = "https://we-are-the-champions.herokuapp.com/enter_result";
const baseURL = "http://127.0.0.1:5000/enter_result";

export default function MatchInformation(props) {
  
  const teamInformation = props.teamInformation;
  const [value, setValue] = React.useState('Controlled');
  const [openGuide, setOpenGuide] = useState(false);

  const handleChange = (event) => {
    setValue(event.target.value);
  };

  function enterResult() {
    const headers = {
      'Content-Type': 'application/json'
    }
    axios.post(baseURL, {
        team_information: teamInformation,
        match_results: value
      }, 
      {
        headers: headers
      })
      .then((response) => {
        props.updateRankingByGroup(response.data.data.ranking_by_group);
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
            label="Enter Match Results Here"
            placeholder="e.g. 
  teamA teamC 1 3
  teamA teamD 2 2"
            minRows={12}
            maxRows={12}
            onChange={handleChange}
            multiline
            fullWidth/>

      </Box>
      <Box
        sx={{px:4, width:"80%"}}> 
        <Stack direction="row" justifyContent="space-between">
          <Button  color="primary"onClick={() => setOpenGuide(state => !openGuide)}> Guide Me</Button>
          <Stack direction="row" >
          <Link to={"/"} style={{ textDecoration: 'none' }}><CircleOutlinedIcon color='primary' fontSize='small'/></Link>
            <CircleIcon color='primary' fontSize='small'/>
            <CircleOutlinedIcon color='primary' fontSize='small'/>
          </Stack>
          <Link to={"/rankings"} style={{ textDecoration: 'none' }}><Button  variant="contained" onClick={enterResult}>Enter</Button></Link>
        </Stack>
        <Collapse in={openGuide}>
            <ul>
              <li>Match Result format must be "Team_name_1 Team_name_2 Team_name_1_score Team_name_2_score"</li>
              <li>Each team is entered in a single line</li>
              <li>Only teams within the same group can play against each other</li>
            </ul>
          </Collapse>
      </Box>
      
    </Box>
  );
}
