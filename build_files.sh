#!/bin/bash

# Create and activate virtual environment
echo "Creating virtual environment..."
python3.9 -m venv venv
source venv/bin/activate

# Update pip
echo "Updating pip..."
python3.9 -m pip install -U pip

# Install dependencies

echo "Installing project dependencies..."
python3.9 -m pip install -r requirements.txt

# Ensure manage.py commands are run from the correct directory
cd /vercel/path0

# Make migrations
echo "Making migrations..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

# Collect staticfiles
echo "Collect static..."
python3.9 manage.py collectstatic --noinput --clear

echo "Build process completed!"