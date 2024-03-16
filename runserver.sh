#!/bin/bash

# Initialize the Virtual Enviormet
cd /home/rafaelcj/Flask_Server
source venv/bin/activate
gunicorn -w 2 -b 192.168.1.109:8000 server:app &

