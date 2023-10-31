import logo from './logo.svg';
import './App.css';
import NetflixData from './DataComponent';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
      <div className={ `container-fluid` }>
        <NetflixData />
      </div>
      <div className={`container-fluid`}>
        <select onChange={(e) => setSelectedDataset(e.target.value)}>
          <option value="Netflix Movies">Netflix</option>
          <option value="Netflix Shows">Jobs</option>
          <option value="IMDb">IMDb</option>
        </select>
        <button onClick={fetchData}>Fetch Data</button>
        {data && <pre>{JSON.stringify(data, null, 2)}</pre>}
      </div>
    </div>
  );
}

export default App;
