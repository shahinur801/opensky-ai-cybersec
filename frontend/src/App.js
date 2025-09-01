import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [aircraftData, setAircraftData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchAircraftData = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.get('/api/aircraft');
      setAircraftData(response.data);
    } catch (err) {
      setError('Failed to fetch aircraft data');
      console.error('Error fetching aircraft data:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchAircraftData();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>OpenSky AI Cybersecurity Monitor</h1>
        <p>Real-time aircraft tracking and security analysis</p>
      </header>
      
      <main className="App-main">
        <div className="controls">
          <button onClick={fetchAircraftData} disabled={loading}>
            {loading ? 'Loading...' : 'Refresh Data'}
          </button>
        </div>

        {error && (
          <div className="error">
            <p>Error: {error}</p>
          </div>
        )}

        <div className="aircraft-grid">
          {aircraftData.length > 0 ? (
            aircraftData.map((aircraft, index) => (
              <div key={index} className="aircraft-card">
                <h3>Aircraft {aircraft.callsign || 'Unknown'}</h3>
                <p><strong>ICAO24:</strong> {aircraft.icao24}</p>
                <p><strong>Country:</strong> {aircraft.origin_country}</p>
                <p><strong>Altitude:</strong> {aircraft.baro_altitude ? `${aircraft.baro_altitude}m` : 'N/A'}</p>
                <p><strong>Velocity:</strong> {aircraft.velocity ? `${aircraft.velocity} m/s` : 'N/A'}</p>
                <p><strong>Position:</strong> 
                  {aircraft.latitude && aircraft.longitude 
                    ? `${aircraft.latitude.toFixed(4)}, ${aircraft.longitude.toFixed(4)}`
                    : 'N/A'
                  }
                </p>
                <p><strong>Last Contact:</strong> 
                  {aircraft.time_position 
                    ? new Date(aircraft.time_position * 1000).toLocaleString()
                    : 'N/A'
                  }
                </p>
              </div>
            ))
          ) : (
            !loading && <p>No aircraft data available</p>
          )}
        </div>
      </main>
    </div>
  );
}

export default App;
