import socket
import threading

HOST = '0.0.0.0'
PORT = 8890

def handle_client(client_socket, addr):
    with client_socket:
        print(f"[ADA] Connected by {addr}")
        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    print(f"[ADA] Connection closed by {addr}")
                    break
                decoded = data.decode('utf-8')
                print(f"[ADA] Received from {addr}: {decoded}")
                # Here you can process or forward data as needed
            except Exception as e:
                print(f"[ADA] Error with {addr}: {e}")
                break

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print(f"[ADA] Server listening on {HOST}:{PORT}")

        while True:
            client_sock, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(client_sock, addr))
            thread.start()

if __name__ == "__main__":
    start_server()
