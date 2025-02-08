# client.py
import socket

# Constants
HOST = '127.0.0.1'
PORT = 12345

def client_program():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        while True:
            print("\nMenu:")
            print("1. Change case")
            print("2. Evaluate expression")
            print("3. Reverse string")
            print("4. Exit")
            choice = input("Enter choice: ")
            
            if choice == '4':
                client.sendall("exit".encode())
                print("Exiting client...")
                break
            
            data = input("Enter data: ")
            client.sendall(f"{choice}:{data}".encode())
            response = client.recv(1024).decode()
            print("Response:", response)

if __name__ == "__main__":
    client_program()