import socket
import os
import threading

# Constants
HOST = '127.0.0.1'
PORT = 12345

# Function to handle client requests
def handle_client(conn, addr):
    print(f"Connected by {addr}")

    while True:
        # Receive the length of the incoming message
        msg_length = conn.recv(16).decode().strip()
        if not msg_length:
            break  # Exit loop if client disconnects

        msg_length = int(msg_length)
        data_received = []

        # Receive full message in chunks
        while msg_length > 0:
            chunk = conn.recv(min(4096, msg_length))  
            if not chunk:
                break
            data_received.append(chunk.decode())
            msg_length -= len(chunk)

        full_message = "".join(data_received)

        # Process (reverse the string)
        response = full_message[::-1]

        # Send response length first
        conn.sendall(str(len(response)).encode().ljust(16))  

        # Send the response in chunks
        for i in range(0, len(response), 4096):
            conn.sendall(response[i:i+4096].encode())

    conn.close()
    print(f"Client {addr} disconnected.")

# Single-Process Server
def single_process_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Reuse address
    server.bind((HOST, PORT)) # Bind to address and port
    server.listen()
    print("Single-Process Server listening...")

    while True:
        conn, addr = server.accept()
        handle_client(conn, addr)

# Multi-Process Server
def multi_process_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print("Multi-Process Server listening...")

    while True:
        conn, addr = server.accept()
        pid = os.fork()
        if pid == 0:  # Child process
            server.close()
            handle_client(conn, addr)
            os._exit(0)  # Child process exits after handling client
        else:
            conn.close()  # Parent process keeps listening for new clients

# Multi-Threaded Server
def multi_threaded_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print("Multi-Threaded Server listening...")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()  # Keep server running and accept new clients


print("Choose Server Type:")
print("1. Single-Process")
print("2. Multi-Process")
print("3. Multi-Threaded")
server_choice = input("Enter choice: ")

if server_choice == '1':
    single_process_server()
elif server_choice == '2':
    multi_process_server()
elif server_choice == '3':
    multi_threaded_server()
else:
    print("Invalid choice")
