import socket
import time
import random

SERVER_HOST = "127.0.0.1"  
SERVER_PORT = 8888

def get_ph_value():
    # Simulate pH sensor reading
    return round(random.uniform(6.0, 8.0), 2)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        while True:
            ph_value = get_ph_value()
            message = f"PH:{ph_value}"
            client_socket.sendall(message.encode("utf-8"))
            print("Sent:", message)
            time.sleep(5)

if __name__ == "__main__":
    main()
