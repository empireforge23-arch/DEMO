#!/bin/bash
echo "📦 Installing Python dependencies..."
pip3 install -r requirements.txt
echo "🚀 Starting the cartoon service..."
python3 app.py