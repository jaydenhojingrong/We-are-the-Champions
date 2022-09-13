import './App.css';
import {BrowserRouter as Router, Routes, Route, Link} from "react-router-dom";
import TeamInformation from "./components/TeamInformation" ;
import MatchInformation from './components/MatchInformation';
import RankingInformation from './components/RankingInformation';
import ButtonAppBar from './components/ButtonAppBar';
import React, {useState} from 'react';

function App() {
  
  const [teamInformation, setTeamInformation] = useState({});
  const updateTeamInformation = newTeamInformation => setTeamInformation(newTeamInformation);

  const [rankingByGroup, setRankingByGroup] = useState({});
  const updateRankingByGroup = newRankingByGroup => setRankingByGroup(newRankingByGroup);
  document.title = "We are the Champions!";

  return (
    
    <Router>
      <Link to={"/"} style={{ textDecoration: 'none' }}><ButtonAppBar /></Link>
      <Routes>
        <Route exact path = "/" element={<TeamInformation teamInformation = {teamInformation} updateTeamInformation = {updateTeamInformation}/>}/>
        <Route path = "/enter_result" element={<MatchInformation teamInformation = {teamInformation} rankingByGroup = {rankingByGroup} updateRankingByGroup = {updateRankingByGroup}/>}/>
        <Route path = "/rankings" element={<RankingInformation rankingByGroup = {rankingByGroup}/>}/>
      </Routes>
    </Router>
  );
}

export default App;
