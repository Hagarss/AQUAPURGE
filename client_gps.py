import socket
import time
import random

SERVER_HOST = "127.0.0.1"  # Change if server is remote
SERVER_PORT = 8888

def get_gps_value():
    # Simulate GPS coordinates (latitude,longitude)
    lat = round(random.uniform(29.9, 30.1), 6)
    lon = round(random.uniform(31.1, 31.3), 6)
    return f"{lat},{lon}"

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        while True:
            gps_value = get_gps_value()
            message = f"GPS:{gps_value}"
            client_socket.sendall(message.encode("utf-8"))
            print("Sent:", message)
            time.sleep(5)

if __name__ == "__main__":
    main()
