from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx
import asyncio
from typing import List, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="OpenSky AI Cybersecurity",
    description="AI-powered cybersecurity platform using OpenSky flight data",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class FlightData(BaseModel):
    icao24: str
    callsign: Optional[str]
    origin_country: str
    time_position: Optional[int]
    last_contact: int
    longitude: Optional[float]
    latitude: Optional[float]
    baro_altitude: Optional[float]
    on_ground: bool
    velocity: Optional[float]
    true_track: Optional[float]
    vertical_rate: Optional[float]
    sensors: Optional[List[int]]
    geo_altitude: Optional[float]
    squawk: Optional[str]
    spi: bool
    position_source: int

class ThreatAlert(BaseModel):
    id: str
    aircraft_id: str
    threat_type: str
    severity: str
    description: str
    timestamp: int
    location: dict

# OpenSky Network API configuration
OPENSKY_API_BASE = "https://opensky-network.org/api"

@app.get("/")
async def root():
    return {"message": "OpenSky AI Cybersecurity Platform API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "opensky-ai-cybersec"}

@app.get("/flights", response_model=List[FlightData])
async def get_flights(bbox: Optional[str] = None):
    """
    Get current flight data from OpenSky Network
    bbox format: "lamin,lomin,lamax,lomax"
    """
    try:
        url = f"{OPENSKY_API_BASE}/states/all"
        params = {}
        if bbox:
            coords = bbox.split(",")
            if len(coords) == 4:
                params["lamin"] = coords[0]
                params["lomin"] = coords[1]
                params["lamax"] = coords[2]
                params["lomax"] = coords[3]
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            
        data = response.json()
        if not data or "states" not in data or not data["states"]:
            return []
        
        flights = []
        for state in data["states"]:
            if len(state) >= 17:
                flight = FlightData(
                    icao24=state[0] or "",
                    callsign=state[1].strip() if state[1] else None,
                    origin_country=state[2] or "",
                    time_position=state[3],
                    last_contact=state[4] or 0,
                    longitude=state[5],
                    latitude=state[6],
                    baro_altitude=state[7],
                    on_ground=state[8] or False,
                    velocity=state[9],
                    true_track=state[10],
                    vertical_rate=state[11],
                    sensors=state[12],
                    geo_altitude=state[13],
                    squawk=state[14],
                    spi=state[15] or False,
                    position_source=state[16] or 0
                )
                flights.append(flight)
        
        logger.info(f"Retrieved {len(flights)} flights")
        return flights
        
    except httpx.HTTPError as e:
        logger.error(f"HTTP error fetching flights: {e}")
        raise HTTPException(status_code=503, detail="Unable to fetch flight data")
    except Exception as e:
        logger.error(f"Error fetching flights: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/threats", response_model=List[ThreatAlert])
async def get_threats():
    """
    Get current threat alerts (mock implementation)
    """
    # This is a mock implementation - in a real system, this would
    # analyze flight data and detect anomalies/threats
    mock_threats = [
        ThreatAlert(
            id="threat-001",
            aircraft_id="ABC123",
            threat_type="unusual_pattern",
            severity="medium",
            description="Aircraft showing unusual flight pattern",
            timestamp=1693920000,
            location={"latitude": 40.7128, "longitude": -74.0060}
        )
    ]
    return mock_threats

@app.post("/analyze")
async def analyze_flight_data():
    """
    Trigger AI analysis of current flight data
    """
    # Mock analysis implementation
    return {
        "status": "analysis_started",
        "message": "AI analysis of flight data initiated",
        "analysis_id": "analysis-001"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
