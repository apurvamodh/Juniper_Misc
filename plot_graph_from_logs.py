import re
import matplotlib.pyplot as plt
from datetime import datetime

# File path to the log file (replace with your actual file path)
log_file_path = "grpc_trace.txt"

# Read the content of the log file
with open(log_file_path, 'r') as file:
    log_data = file.read()

# Regular expressions for matching connection and disconnection logs
connect_regex = r"(\w+ \d+ \d+:\d+:\d+) CreateClientInfo: client info for peer (.+) created successfully"
disconnect_regex = r"(\w+ \d+ \d+:\d+:\d+) DestroyClientInfo: peer (.+) deleted from client map"

# Extract connection and disconnection events
connect_events = re.findall(connect_regex, log_data)
disconnect_events = re.findall(disconnect_regex, log_data)

# Convert timestamps to datetime objects
connect_times = [(datetime.strptime(event[0], "%b %d %H:%M:%S"), 'connect') for event in connect_events]
disconnect_times = [(datetime.strptime(event[0], "%b %d %H:%M:%S"), 'disconnect') for event in disconnect_events]

# Combine and sort events by time
events = sorted(connect_times + disconnect_times, key=lambda x: x[0])

# Prepare data for plotting
times = [event[0] for event in events]
connections = []
current_connections = 0

for event in events:
    if event[1] == 'connect':
        current_connections += 1
    elif event[1] == 'disconnect':
        current_connections -= 1
    connections.append(current_connections)

# Plot the graph
plt.figure(figsize=(10, 5))
plt.plot(times, connections, marker='o')
plt.xlabel('Time')
plt.ylabel('Number of Connections')
plt.title('Client Connections and Disconnections Over Time')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('graph.png')
