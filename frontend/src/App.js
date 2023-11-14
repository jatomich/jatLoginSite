import logo from './logo.svg';
import './styles/App.css';
import NetflixData from './components/DataComponent';

import Container from 'react-bootstrap/Container';
import MyNav from './components/MyNav';
// import Nav from 'react-bootstrap/Nav';


function App() {
  return (
    <div className="App">
      <Container>
        <MyNav />
      </Container>
      <header id="top-latch" className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Netflix Movies and TV Shows.
        </p>
      </header>
      <Container>
        <NetflixData />
      </Container>
      {/* <div className={`container-fluid`}>
        <select onChange={(e) => setSelectedDataset(e.target.value)}>
          <option value="Netflix Movies">Netflix</option>
          <option value="Netflix Shows">Jobs</option>
          <option value="IMDb">IMDb</option>
        </select>
        <button onClick={fetchData}>Fetch Data</button>
        {data && <pre>{JSON.stringify(data, null, 2)}</pre>}
      </div> */}
      <script src="https://cdn.jsdelivr.net/npm/react/umd/react.production.min.js" crossOrigin="true"></script>

      <script
        src="https://cdn.jsdelivr.net/npm/react-dom/umd/react-dom.production.min.js"
        crossOrigin="true"></script>

      <script
        src="https://cdn.jsdelivr.net/npm/react-bootstrap@next/dist/react-bootstrap.min.js"
        crossOrigin="true"></script>

      <script>var Alert = ReactBootstrap.Alert;</script>
    </div>
  );
}

export default App;
