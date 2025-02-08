# Computer-Networks-T-1

# Client-Server Task Processing & Benchmarking

## Overview
This project consists of two primary problems:
1. **Client-Server Task Processing**: A client interacts with a server that processes different tasks such as case conversion, mathematical expression evaluation, and string reversal.
2. **Client-Server Benchmarking**: A benchmarking task measures the performance of different server implementations by running multiple concurrent clients and recording execution time.

---
## Problem 1: Client-Server Task Processing
This implementation consists of a client (`client.py`) and a server (`server.py`) that can run in three different modes:

### Server (`server.py`)
The server supports three modes of operation:
1. **Single-Process Server**: Handles one client at a time.
2. **Multi-Process Server**: Creates a new process for each connected client.
3. **Multi-Threaded Server**: Creates a new thread for each connected client.

#### Running the Server:
```bash
python3 server.py
```
You will be prompted to select the server mode:
```
Choose Server Type:
1. Single-Process
2. Multi-Process
3. Multi-Threaded
Enter choice:
```

### Client (`client.py`)
The client interacts with the server by selecting one of the following options:
1. Change the case of a string.
2. Evaluate a mathematical expression.
3. Reverse a string.
4. Exit.

#### Running the Client:
```bash
python3 client.py
```

---
## Problem 2: Client-Server Benchmarking
This problem evaluates the performance of different server architectures by running multiple concurrent clients and measuring execution time.

### Server (`server2.py`)
Like `server.py`, this server also has three modes:
- Single-Process
- Multi-Process
- Multi-Threaded

It processes client requests by reversing a string after a **3-second delay**.

#### Running the Server:
```bash
python3 server2.py
```
Select the server type when prompted.

### Client (`client2.py`)
This client sends a large string to the server and receives the reversed string.

#### Running the Client:
```bash
python3 client2.py
```

### Benchmarking (`benchmarking.py`)
The benchmarking script automates the testing process by:
1. Running `server2.py` in different modes.
2. Executing multiple instances of `client2.py` using `start.sh`.
3. Measuring execution time.
4. Plotting performance results.

#### Running the Benchmarking Script:
```bash
python3 benchmarking.py
```

### Bash Script (`start.sh`)
Before running the bash script, ensure that the server (`server2.py`) is already running.

#### Usage:
```bash
bash start.sh client2.py 10
```
This runs `client2.py` **10 times concurrently**.This script runs multiple client instances in parallel.

#### Usage:
```bash
bash start.sh client2.py 10
```
This runs `client2.py` **10 times concurrently**.

### Performance Evaluation
The benchmarking script:
- Runs tests with **10 to 100 concurrent clients**.
- Records execution times in `latency_results3.txt`.
- Generates a performance plot.

### Expected Graph Output
- **X-axis**: Number of concurrent clients (10, 20, ..., 100).
- **Y-axis**: Execution time (latency).

This allows performance comparison between different server architectures.

---
### Client2.py Note
A long string has been hardcoded in `client2.py` and used to showcase the difference between the three types of servers.- `server.py` and `client.py` implement a general task-processing client-server model.
- `server2.py`, `client2.py`, and `benchmarking.py` facilitate benchmarking for different server architectures.
- The project demonstrates the trade-offs between single-process, multi-process, and multi-threaded server designs in terms of performance.


