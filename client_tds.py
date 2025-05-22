import socket
import time
import random

SERVER_HOST = "127.0.0.1"  
SERVER_PORT = 8888

def get_tds_value():
    # Simulate TDS sensor reading
    return round(random.uniform(200.0, 500.0), 2)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        while True:
            tds_value = get_tds_value()
            message = f"TDS:{tds_value}"
            client_socket.sendall(message.encode("utf-8"))
            print("Sent:", message)
            time.sleep(5)

if __name__ == "__main__":
    main()
