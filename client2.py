import socket
import argparse
import time

HOST = '127.0.0.1'
PORT = 12345
CHUNK_SIZE = 1024

# parser = argparse.ArgumentParser(description="Client Program")
# parser.add_argument("client_number", type=int, help="Client number")
# args = parser.parse_args()

# with open(args.filename, "r") as file:
#     input_text = file.read()
input_text = "Hello, World!" * 1000000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


# Send message length first

client.sendall(str(len(input_text)).encode().ljust(16))  
start = time.time()
# Send the message in chunks
for i in range(0, len(input_text), CHUNK_SIZE):
    client.sendall(input_text[i:i+CHUNK_SIZE].encode())

time.sleep(3) # 3 seconds delay
# Receive response length first
response_length = int(client.recv(16).decode().strip())
response_data = []

# Receive response in chunks
while response_length > 0:
    chunk = client.recv(min(CHUNK_SIZE, response_length))
    if not chunk:
        break
    response_data.append(chunk.decode())
    response_length -= len(chunk)

end = time.time()

response = "".join(response_data)
# print("Server response received in {:.6f} seconds.".format(end - start))

client.close()  # Client closes connection, but server stays running
# print(f"Response from server: {response}")