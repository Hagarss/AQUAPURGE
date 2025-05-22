import socket
import time
import random

SERVER_HOST = "127.0.0.1" 
SERVER_PORT = 8888

def get_adafruit_data():
    # Simulate Adafruit Cloud data, e.g., pump status or other sensor values
    # For demonstration, let's say it sends a random integer status 0 or 1
    return random.choice([0, 1])

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        while True:
            data = get_adafruit_data()
            message = f"ADA:{data}"
            client_socket.sendall(message.encode("utf-8"))
            print("Sent:", message)
            time.sleep(5)

if __name__ == "__main__":
    main()
