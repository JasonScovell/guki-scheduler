#!/bin/bash

echo "Call Schedule Generator"
echo "====================="
echo ""
echo "Starting application..."
echo ""

# Check if Python is available
if command -v python3 &> /dev/null; then
    python3 run_app.py
elif command -v python &> /dev/null; then
    python run_app.py
else
    echo "Error: Python is not installed or not in PATH"
    echo "Please install Python 3.7 or higher"
    echo ""
    read -p "Press Enter to exit..."
fi 