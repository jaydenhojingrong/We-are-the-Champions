import './App.css';
import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import TeamInformation from "./components/TeamInformation" ;
import ButtonAppBar from './components/ButtonAppBar';


function App() {
  return (
    <Router>
      <ButtonAppBar />
      <Routes>
        <Route exact path = "/" element={<TeamInformation />}/>
        <Route path = "/try" element={<TeamInformation />}/>
      </Routes>
    </Router>
  );
}

export default App;
