import React from 'react'; 
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import PropTypes from 'prop-types';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import DoneOutlineTwoToneIcon from '@mui/icons-material/DoneOutlineTwoTone';
import CloseTwoToneIcon from '@mui/icons-material/CloseTwoTone';
import CircleOutlinedIcon from '@mui/icons-material/CircleOutlined';
import CircleIcon from '@mui/icons-material/Circle';
import Stack from "@mui/material/Stack"
import { Link } from "react-router-dom";

function createData(rank, result, name) {
    return { rank, result, name };
  }
function TabPanel(props) {
    const { children, value, index, ...other } = props;

    return (
    <div
        role="tabpanel"
        hidden={value !== index}
        id={`simple-tabpanel-${index}`}
        aria-labelledby={`simple-tab-${index}`}
        {...other}
    >
        {value === index && (
        <Box sx={{ p: 3 }}>
            <Typography>{children}</Typography>
        </Box>
        )}
    </div>
    );
}

TabPanel.propTypes = {
    children: PropTypes.node,
    index: PropTypes.number.isRequired,
    value: PropTypes.number.isRequired,
};

function a11yProps(index) {
    return {
    id: `simple-tab-${index}`,
    'aria-controls': `simple-tabpanel-${index}`,
    };
}
export default function RankingInformation(props) {

    const groups = [[], []];
    const groupNames = [];
    var index = 0;
    
    console.log(props.rankingByGroup);
    
    for (var key in props.rankingByGroup){
        groupNames.push(key);
        groups[index] = props.rankingByGroup[key];
        index++;
    }

    const [value, setValue] = React.useState(0);

    const handleChange = (event, newValue) => {
        setValue(newValue);
    };

    var rowsGroup1 = [];
    for (let ranking = 0; ranking < groups[0].length; ranking++) {
        rowsGroup1.push(createData(ranking + 1, ranking < 4 ? true : false, groups[0][ranking]))
    } 

    var rowsGroup2 = [];
    for (let ranking = 0; ranking < groups[1].length; ranking++) {
        rowsGroup2.push(createData(ranking + 1, ranking < 4 ? true : false, groups[1][ranking]))
    } 

    return (
        <Box>
            <Box justifyContent="center" sx={{ width: '60%' }}>
                <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
                    <Tabs value={value} onChange={handleChange} aria-label="basic tabs example">
                    <Tab label={"Group: " + groupNames[0]} {...a11yProps(0)} />
                    <Tab label={"Group: " + groupNames[1]} {...a11yProps(1)} />
                    </Tabs>
                </Box>
                <TabPanel value={value} index={0}>
                    <TableContainer component={Paper}>
                        <Table sx={{ minWidth: 650 }} aria-label="simple table">
                            <TableHead>
                                <TableRow>
                                    <TableCell style={{ width: "10%" }}><b>Ranking</b></TableCell>
                                    <TableCell style={{ width: "25%" }} align="right"><b>Passed?</b></TableCell>
                                    <TableCell  style={{ width: "25%" }} align="right"><b>Team</b></TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {rowsGroup1.map((row1) => (
                                <TableRow
                                    key={row1.name}
                                    sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                                >
                                    <TableCell component="th" scope="row">
                                        {row1.rank}
                                    </TableCell>
                                    {row1.result 
                                        ? <TableCell align="right"><DoneOutlineTwoToneIcon style={{ color: 'green' }} /></TableCell>
                                        : <TableCell align="right"><CloseTwoToneIcon style={{ color: 'red' }} /></TableCell>
                                    }
                                    <TableCell align="right">{row1.name}</TableCell>
                            
                                </TableRow>
                                ))} 
                            </TableBody>
                        </Table>
                    </TableContainer>
                </TabPanel>
                <TabPanel value={value} index={1}>
                <TableContainer component={Paper}>
                        <Table sx={{ minWidth: 650 }} aria-label="simple table">
                            <TableHead>
                                <TableRow>
                                    <TableCell style={{ width: "10%" }}><b>Ranking</b></TableCell>
                                    <TableCell style={{ width: "25%" }} align="right"><b>Passed?</b></TableCell>
                                    <TableCell style={{ width: "25%" }} align="right"><b>Team</b></TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {rowsGroup2.map((row2) => (
                                <TableRow
                                    key={row2.name}
                                    sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                                >
                                    <TableCell component="th" scope="row">
                                        {row2.rank}
                                    </TableCell>
                                    {row2.result 
                                        ? <TableCell align="right"><DoneOutlineTwoToneIcon style={{ color: 'green' }} /></TableCell>
                                        : <TableCell align="right"><CloseTwoToneIcon style={{ color: 'red' }} /></TableCell>
                                    }
                                    <TableCell align="right">{row2.name}</TableCell>
                            
                                </TableRow>
                                ))} 
                            </TableBody>
                        </Table>
                    </TableContainer>
                </TabPanel>
                <Box display="flex" justifyContent="center" alignItems="center" sx={{p:2}}>
                    <Stack direction="row" >
                        <Link to={"/"} style={{ textDecoration: 'none' }}><CircleOutlinedIcon color='primary' fontSize='small'/></Link>
                        <Link to={"/enter_result"} style={{ textDecoration: 'none' }}><CircleOutlinedIcon color='primary' fontSize='small'/></Link>
                        <CircleIcon color='primary' fontSize='small'/>
                    </Stack>
                </Box>
            </Box>
        </Box>
        
    );
}
