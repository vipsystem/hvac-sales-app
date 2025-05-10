#!/bin/bash

# Backend Setup
cd /Users/kevinaustin/CascadeProjects/hvac-sales-app/backend

# Create virtual environment if not exists
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install backend dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional, interactive)
echo "Creating Django superuser (optional)"
python manage.py createsuperuser

# Start Django development server in background
python manage.py runserver 8000 &
BACKEND_PID=$!

# Frontend Setup
cd ../frontend/hvac-sales-frontend

# Install frontend dependencies
npm install

# Start React development server
npm start

# Function to cleanup background processes
cleanup() {
    echo "Stopping background processes..."
    kill $BACKEND_PID
    deactivate
}

# Trap exit signals to cleanup
trap cleanup EXIT

# Wait for user input to exit
read -p "Press Enter to stop the servers..."
