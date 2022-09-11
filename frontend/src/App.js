import './App.css';
import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import MultilineTextFields from "./components/MultilineTextFields" ;
import ButtonAppBar from './components/ButtonAppBar';

function App() {
  return (
    <Router>
      <ButtonAppBar />
      <Routes>
        <Route exact path = "/" element={<MultilineTextFields />}/>
      </Routes>
    </Router>
  );
}

export default App;
