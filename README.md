# HVAC Sales Management Application

## Overview
A comprehensive web application for managing HVAC product sales, user authentication, and quote generation.

## Tech Stack
- Backend: Django, Django Rest Framework
- Frontend: React, Redux
- Database: PostgreSQL
- Authentication: Token-based

## Features
- User Registration and Authentication
- Product Management
- Sales Quote Creation and Tracking
- Role-based Access Control

## Local Development Setup Guide

### 1. Prerequisites
- Python 3.9+
- Node.js 14+
- pip
- npm
- PostgreSQL (optional, SQLite used by default)

### 2. Environment Configuration
1. Navigate to `backend/` directory
2. Create `.env` file from `.env.example`
3. Customize configuration as needed

### 3. Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

### 4. Frontend Setup
```bash
# Navigate to frontend directory
cd frontend/hvac-sales-frontend

# Install dependencies
npm install
```

### 5. Running the Application
- Backend: `python manage.py runserver`
- Frontend: `npm start`

### 6. Debugging Common Issues
- Ensure all dependencies are installed
- Check `.env` file configurations
- Verify Python and Node.js versions

### 7. Quick Start Script
Use the provided `local_setup.sh` script for automated setup:
```bash
./local_setup.sh
```

### 8. Accessing the Application
- Backend API: `http://localhost:8000/api/`
- Frontend: `http://localhost:3000`

## Environment Variables
- Create `.env` files in backend and frontend directories
- Add necessary configuration variables

## Deployment
- Backend: Heroku/DigitalOcean
- Frontend: Netlify/Vercel
- Database: PostgreSQL hosting

## Contributing
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create pull request
