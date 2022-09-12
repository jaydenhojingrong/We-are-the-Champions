import './App.css';
import {BrowserRouter as Router, Routes, Route, Link} from "react-router-dom";
import TeamInformation from "./components/TeamInformation" ;
import MatchInformation from './components/MatchInformation';
import ButtonAppBar from './components/ButtonAppBar';
import React, {useState} from 'react';

function App() {
  
  const [teamInformation, setTeamInformation] = useState({"placeholder": "placeholder"});
  const updateTeamInformation = newTeamInformation => setTeamInformation(newTeamInformation);

  const [rankingByGroup, setRankingByGroup] = useState({"placeholder": "placeholder"});
  const updateRankingByGroup = newRankingByGroup => setRankingByGroup(newRankingByGroup);

  return (
    <Router>
      <Link to={"/"} style={{ textDecoration: 'none' }}><ButtonAppBar /></Link>
      <Routes>
        <Route exact path = "/" element={<TeamInformation teamInformation = {teamInformation} updateTeamInformation = {updateTeamInformation}/>}/>
        <Route path = "/enter_result" element={<MatchInformation teamInformation = {teamInformation} rankingByGroup = {rankingByGroup} updateRankingByGroup = {updateRankingByGroup}/>}/>
        <Route path = "/rankings" element={<MatchInformation rankingByGroup = {rankingByGroup}/>}/>
      </Routes>
    </Router>
  );
}

export default App;
