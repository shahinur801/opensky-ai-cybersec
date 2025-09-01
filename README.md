Made by Shahinur Islam.

# OpenSky AI Cybersecurity

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org) [![React](https://img.shields.io/badge/React-18.2.0-blue.svg)](https://reactjs.org) [![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green.svg)](https://fastapi.tiangolo.com)

A real-time aircraft tracking and cybersecurity analysis system that leverages the OpenSky Network API to monitor aircraft movements and detect potential security threats using AI-powered analytics.

## 🌟 Features

- **Real-time Aircraft Tracking**: Monitor live aircraft positions using OpenSky Network data
- **AI-Powered Security Analysis**: Advanced threat detection and anomaly identification
- **Interactive Dashboard**: Modern React-based web interface for monitoring and analysis
- **RESTful API**: Comprehensive API for data access and system integration
- **Data Visualization**: Interactive charts and maps for better air traffic understanding
- **Threat Detection**: Identify unusual flight patterns, airspace violations, and anomalies
- **Real-time Alerts**: Configurable notification system with severity levels

## 🏗️ Architecture

### Backend

- **Framework**: FastAPI (Python) for high-performance async API
- **Database**: Ready for PostgreSQL/MongoDB integration
- **API Client**: OpenSky Network REST API integration
- **AI/ML**: TensorFlow/PyTorch support for threat detection algorithms
- **Authentication**: JWT-based security system

### Frontend

- **Framework**: React.js 18+ with modern hooks
- **Styling**: Responsive CSS3 design
- **State Management**: React Context API
- **Charts**: Chart.js for data visualization
- **Maps**: Ready for Leaflet/MapBox integration
- **HTTP Client**: Axios for API communication

## 🚀 Quick Start

### Prerequisites

Ensure you have the following installed:

- Python 3.8+ (Python 3.9+ recommended)
- Node.js 16+ (Node.js 18+ recommended)
- npm or yarn package manager
- Git for version control

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shahinur801/opensky-ai-cybersec.git
   cd opensky-ai-cybersec
   ```

2. **Backend Setup:**
   ```bash
   cd backend
   
   # Create virtual environment (recommended)
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Start the FastAPI server
   uvicorn main:app --reload --host 0.0.0.0 --port 5000
   ```

3. **Frontend Setup (in a new terminal):**
   ```bash
   cd frontend
   
   # Install dependencies
   npm install
   
   # Start the React development server
   npm start
   ```

4. **Access the Application:**
   - **Frontend**: http://localhost:3000
   - **Backend API**: http://localhost:5000
   - **API Documentation**: http://localhost:5000/docs

## 📚 API Documentation

### Aircraft Data Endpoints

- `GET /api/aircraft` - Retrieve current aircraft data
- `GET /api/aircraft/{icao24}` - Get specific aircraft information
- `GET /api/threats` - Get detected security threats
- `GET /api/aircraft/search?query={query}` - Search aircraft by criteria

### System Endpoints

- `GET /api/health` - System health check
- `GET /api/stats` - System statistics and metrics
- `GET /api/alerts` - Get system alerts
- `POST /api/alerts/configure` - Configure alert settings

### Authentication Endpoints

- `POST /api/auth/login` - User authentication
- `POST /api/auth/refresh` - Token refresh
- `GET /api/auth/profile` - User profile information

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the backend directory:

```env
# OpenSky Network API credentials (optional but recommended)
OPENSKY_USERNAME=your_username
OPENSKY_PASSWORD=your_password

# Database configuration
DATABASE_URL=postgresql://localhost/opensky_db
# or for SQLite (development)
# DATABASE_URL=sqlite:///./opensky.db

# Security
SECRET_KEY=your-super-secure-secret-key-here
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Application settings
API_HOST=0.0.0.0
API_PORT=5000
DEBUG=true

# External API rate limits
API_RATE_LIMIT=100
CACHE_TIMEOUT=300
```

### Frontend Configuration

Create a `.env` file in the frontend directory:

```env
# API endpoints
REACT_APP_API_BASE_URL=http://localhost:5000
REACT_APP_API_TIMEOUT=10000

# Feature flags
REACT_APP_ENABLE_MAPS=true
REACT_APP_ENABLE_ALERTS=true

# Application settings
REACT_APP_REFRESH_INTERVAL=30000
REACT_APP_MAX_AIRCRAFT_DISPLAY=1000
```

## 🔒 Security Features

### Threat Detection Algorithms

- **Flight Pattern Analysis**: Detect unusual or suspicious flight patterns
- **Airspace Violation Detection**: Monitor restricted airspace violations
- **Speed & Altitude Anomalies**: Identify aircraft operating outside normal parameters
- **Communication Blackouts**: Detect aircraft with lost communication signals
- **Route Deviation Analysis**: Monitor significant route deviations

### Alert System

- **Severity Levels**: Low, Medium, High, Critical threat classifications
- **Real-time Notifications**: Instant alerts for security threats
- **Configurable Thresholds**: Customizable detection sensitivity
- **Integration Ready**: API endpoints for external security systems

## 🧪 Testing

### Backend Tests

```bash
cd backend

# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_aircraft.py
```

### Frontend Tests

```bash
cd frontend

# Run all tests
npm test

# Run tests with coverage
npm test -- --coverage

# Run tests in watch mode
npm test -- --watch
```

## 🚢 Deployment

### Docker Deployment

1. **Build and run with Docker Compose:**
   ```bash
   docker-compose up --build
   ```

2. **Production deployment:**
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

### Manual Deployment

1. **Backend Production Setup:**
   ```bash
   cd backend
   pip install -r requirements.txt
   gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:5000
   ```

2. **Frontend Production Build:**
   ```bash
   cd frontend
   npm run build
   # Serve the build folder with nginx or any static file server
   ```

## 🤝 Contributing

We welcome contributions to the OpenSky AI Cybersecurity project!

### Development Workflow

1. Fork the repository
2. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and add tests
4. **Run the test suite:**
   ```bash
   # Backend tests
   cd backend && pytest
   
   # Frontend tests
   cd frontend && npm test
   ```
5. **Commit your changes:**
   ```bash
   git commit -m "Add your descriptive commit message"
   ```
6. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```
7. Create a Pull Request

### Code Style Guidelines

- **Python**: Follow PEP 8 standards, use Black for formatting
- **JavaScript**: Follow Airbnb style guide, use Prettier for formatting
- **Commit Messages**: Use conventional commit format
- **Documentation**: Update relevant documentation for new features

## 📖 Documentation

Detailed documentation is available in the `/docs` directory:

- [API Documentation](docs/api.md)
- [Deployment Guide](docs/deployment.md)
- [Security Features](docs/security.md)
- [Development Setup](docs/development.md)

For comprehensive documentation, visit: [Documentation](docs/index.md)

## 🗺️ Roadmap

- [ ] **Enhanced ML Models**: Advanced machine learning algorithms for threat detection
- [ ] **Mobile Application**: iOS and Android apps for mobile monitoring
- [ ] **Multi-user Dashboard**: Role-based access control and user management
- [ ] **Integration APIs**: Connect with aviation authorities and security systems
- [ ] **Advanced Analytics**: Historical data analysis and trend prediction
- [ ] **Geofencing**: Custom airspace monitoring and alerts
- [ ] **Real-time Collaboration**: Multi-user real-time monitoring capabilities

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **GitHub Repository**: [https://github.com/shahinur801/opensky-ai-cybersec](https://github.com/shahinur801/opensky-ai-cybersec)
- **OpenSky Network**: [https://opensky-network.org/](https://opensky-network.org/)
- **FastAPI Documentation**: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
- **React Documentation**: [https://reactjs.org/](https://reactjs.org/)

## 💬 Support

- **Issues**: [GitHub Issues](https://github.com/shahinur801/opensky-ai-cybersec/issues)
- **Discussions**: [GitHub Discussions](https://github.com/shahinur801/opensky-ai-cybersec/discussions)
- **Security**: For security-related issues, please see [SECURITY.md](SECURITY.md)

## 🙏 Acknowledgments

- **OpenSky Network** for providing free aircraft tracking data
- **FastAPI** for the excellent Python web framework
- **React** for the powerful frontend library
- **Contributors** who help improve this project

---

**Note**: This project is for educational and research purposes. Ensure compliance with local aviation regulations and data privacy laws when deploying in production environments.

Made by Shahinur Islam.
