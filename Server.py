import socket
import threading

def handle_client(client_socket, address):
    print(f"Connected: {address}")

    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print(f"Client ({address}): {message}")
            broadcast(message)
        except Exception as e:
            print(f"Error: {e}")
            break

    print(f"Disconnected: {address}")
    client_socket.close()

def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode("utf-8"))
        except Exception as e:
            print(f"Error broadcasting message: {e}")
            clients.remove(client)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 9999))
    server_socket.listen(5)
    print("Server started, waiting for connections...")

    while True:
        client_socket, address = server_socket.accept()
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

clients = []

if __name__ == "__main__":
    start_server()
