import socket
import time
import random

SERVER_HOST = "127.0.0.1"  # Update if needed
SERVER_PORT = 8888

def get_belt_status():
    # Simulate conveyor belt status (0=stopped, 1=running)
    return random.choice([0, 1])

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        while True:
            status = get_belt_status()
            message = f"BELT:{status}"
            client_socket.sendall(message.encode("utf-8"))
            print("Sent:", message)
            time.sleep(5)

if __name__ == "__main__":
    main()
