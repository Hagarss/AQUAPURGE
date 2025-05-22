# server_socket.py
# Server to receive data from clients (GPS, TDS, pH) and forward to Adafruit

import socket
import threading
import json
import time
import requests

# Replace with your Adafruit IO credentials
ADAFRUIT_IO_USERNAME = "Hagar_Soliman"
ADAFRUIT_IO_KEY = "aio_VZsZ123example456keyXYZ"

# Adafruit IO Feed URLs
feed_urls = {
    'gps': f'https://io.adafruit.com/api/v2/{ADAFRUIT_IO_USERNAME}/feeds/gps/data',
    'tds': f'https://io.adafruit.com/api/v2/{ADAFRUIT_IO_USERNAME}/feeds/tds/data',
    'ph': f'https://io.adafruit.com/api/v2/{ADAFRUIT_IO_USERNAME}/feeds/ph/data'
}

def post_to_adafruit(feed, value):
    url = feed_urls[feed]
    headers = {'X-AIO-Key': ADAFRUIT_IO_KEY, 'Content-Type': 'application/json'}
    data = {'value': value}
    try:
        requests.post(url, headers=headers, json=data)
    except Exception as e:
        print(f"[ERROR] Failed to post to Adafruit: {e}")

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} c
