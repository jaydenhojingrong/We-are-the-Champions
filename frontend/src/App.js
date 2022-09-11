import './App.css';
import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import TeamInformation from "./components/TeamInformation" ;
import MatchInformation from './components/MatchInformation';
import ButtonAppBar from './components/ButtonAppBar';


function App() {
  return (
    <Router>
      <ButtonAppBar />
      <Routes>
        <Route exact path = "/" element={<TeamInformation />}/>
        <Route path = "/enter_result" element={<MatchInformation />}/>
      </Routes>
    </Router>
  );
}

export default App;
