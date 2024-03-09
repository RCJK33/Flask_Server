# Initialize the Virtual Enviormet
source venv/bin/activate
gunicorn -w 2 -b 192.168.1.109 server:app
