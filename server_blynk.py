import socket
import threading

HOST = '0.0.0.0'
PORT = 8891

def handle_client(client_socket, addr):
    with client_socket:
        print(f"[Blynk] Connected by {addr}")
        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    print(f"[Blynk] Connection closed by {addr}")
                    break
                decoded = data.decode('utf-8')
                print(f"[Blynk] Received from {addr}: {decoded}")
                # Interpret commands and control devices accordingly
                # e.g., "PUMP:ON" or "BELT:OFF"
            except Exception as e:
                print(f"[Blynk] Error with {addr}: {e}")
                break

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print(f"[Blynk] Server listening on {HOST}:{PORT}")

        while True:
            client_sock, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(client_sock, addr))
            thread.start()

if __name__ == "__main__":
    start_server()
