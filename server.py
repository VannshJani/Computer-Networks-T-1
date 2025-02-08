# server.py
import socket
import os
import threading
import multiprocessing

# Constants
HOST = '127.0.0.1'
PORT = 12345

# Function to handle client requests
def handle_client(conn, addr):
    print(f"Connected by {addr}")
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data or data.lower() == 'exit':
                print(f"Client {addr} disconnected.")
                break
            
            command, value = data.split(':', 1)
            if command == '1':
                response = value.swapcase()
            elif command == '2':
                try:
                    response = str(eval(value))
                except Exception:
                    response = "Error in expression"
            elif command == '3':
                response = value[::-1]
            else:
                response = "Invalid option"
            
            conn.sendall(response.encode())
        except Exception as e:
            print(f"Error: {e}")
            break
    conn.close()

# Single-Process Server
def single_process_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print("Single-Process Server listening...")
    
    while True:
        conn, addr = server.accept()
        handle_client(conn, addr)

# Multi-Process Server
def multi_process_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print("Multi-Process Server listening...")
    
    while True:
        conn, addr = server.accept()
        process = multiprocessing.Process(target=handle_client, args=(conn, addr))
        process.start()
        conn.close()

# Multi-Threaded Server
def multi_threaded_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print("Multi-Threaded Server listening...")
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
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
