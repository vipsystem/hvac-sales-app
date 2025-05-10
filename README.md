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

## Setup Instructions

### Backend Setup
1. Navigate to `backend/`
2. Create a virtual environment: `python3 -m venv venv`
3. Activate venv: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Start server: `python manage.py runserver`

### Frontend Setup
1. Navigate to `frontend/hvac-sales-frontend/`
2. Install dependencies: `npm install`
3. Start development server: `npm start`

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
