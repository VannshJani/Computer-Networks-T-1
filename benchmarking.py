import subprocess
import time
import matplotlib.pyplot as plt

# Define server options
server_options = {
    "Single-Process": "1",
    "Multi-Process": "2",
    "Multi-Threaded": "3"
}

server_script = "server2.py"
client_script = "client2.py"
start_script = "start.sh"
concurrent_clients = list(range(10, 110, 10))
results = {server: [] for server in server_options}

# Open a file to save latency results
with open("latency_results3.txt", "w") as file:
    file.write("Server Type,Number of Clients,Execution Time (Seconds)\n")

    for server_name, server_mode in server_options.items():
        print(f"Benchmarking {server_name}...")
        
        # Start the server
        server_process = subprocess.Popen(["python3", server_script], stdin=subprocess.PIPE)
        time.sleep(2)  # Allow server to initialize
        server_process.stdin.write(f"{server_mode}\n".encode())
        server_process.stdin.flush()
        
        for clients in concurrent_clients:
            print(f"Running with {clients} clients...")
            start_time = time.time()
            
            # Run benchmarking script
            subprocess.run(["bash", start_script, client_script, str(clients)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            elapsed_time = time.time() - start_time
            results[server_name].append(elapsed_time)
            
            # Save results to file
            file.write(f"{server_name},{clients},{elapsed_time:.4f}\n")
        
        # Stop the server
        server_process.terminate()
        server_process.wait()

# Plot results
plt.figure(figsize=(10, 6))
for server_name, times in results.items():
    plt.plot(concurrent_clients, times, label=server_name, marker='o')

plt.xlabel("Number of Concurrent Clients")
plt.ylabel("Execution Time (Seconds)")
plt.title("Server Performance Benchmark")
plt.legend()
plt.grid()
plt.show()
