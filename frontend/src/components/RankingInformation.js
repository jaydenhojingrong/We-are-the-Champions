import React, {useState}  from 'react'; 
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
import { Link } from "react-router-dom";
import DoneOutlineTwoToneIcon from '@mui/icons-material/DoneOutlineTwoTone';
import CloseTwoToneIcon from '@mui/icons-material/CloseTwoTone';

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

    const group1 = props.rankingByGroup["1"];
    const group2 = props.rankingByGroup["2"];
    
    console.log(props.rankingByGroup);
    
    for (var key in props.rankingByGroup){
        console.log( key );
        console.log(props.rankingByGroup[key]);
    }

    const [value, setValue] = React.useState(0);

    const handleChange = (event, newValue) => {
        setValue(newValue);
    };

    var rowsGroup1 = [];
    var ranking = 1;
    ranking ++;
    for (let ranking = 0; ranking < group1.length; ranking++) {
        rowsGroup1.push(createData(ranking + 1, ranking < 4 ? true : false, group1[ranking]))
    } 
    console.log(rowsGroup1);

    return (
        <Box>
            <Box justifyContent="center" sx={{ width: '80%' }}>
                <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
                    <Tabs value={value} onChange={handleChange} aria-label="basic tabs example">
                    <Tab label="Item One" {...a11yProps(0)} />
                    <Tab label="Item Two" {...a11yProps(1)} />
                    <Tab label="Item Three" {...a11yProps(2)} />
                    </Tabs>
                </Box>
                <TabPanel value={value} index={0}>
                    <TableContainer component={Paper}>
                        <Table sx={{ minWidth: 650 }} aria-label="simple table">
                            <TableHead>
                                <TableRow>
                                    <TableCell><b>Ranking</b></TableCell>
                                    <TableCell align="right"><b>Passed?</b></TableCell>
                                    <TableCell align="right"><b>Team</b></TableCell>
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
                    Item Two
                </TabPanel>
                <TabPanel value={value} index={2}>
                    Item Three
                </TabPanel>
            </Box>
        </Box>
        
    );
}
