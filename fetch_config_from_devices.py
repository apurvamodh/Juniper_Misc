from jnpr.junos import Device
from jnpr.junos.exception import ConnectError

# List of devices with connection details
devices = [
    {'host': '10.85.149.152', 'user': 'username1', 'password': 'password1'},
    {'host': '10.85.149.153', 'user': 'username2', 'password': 'password2'},
    {'host': '10.85.149.154', 'user': 'username1', 'password': 'password1'},
    {'host': '10.85.149.155', 'user': 'username2', 'password': 'password2'},
    {'host': '10.85.149.162', 'user': 'username1', 'password': 'password1'},
    {'host': '10.85.149.164', 'user': 'username2', 'password': 'password2'},
    {'host': '10.85.149.165', 'user': 'username1', 'password': 'password1'},
    {'host': '10.85.149.179', 'user': 'username2', 'password': 'password2'},
    {'host': '10.85.149.180', 'user': 'username1', 'password': 'password1'},
    {'host': '10.85.149.181', 'user': 'username1', 'password': 'password1'},
    {'host': '10.85.149.182', 'user': 'username1', 'password': 'password1'},
    {'host': '10.85.149.187', 'user': 'username1', 'password': 'password1'},
]

def fetch_config(device_info):
    try:
        # Establish a connection to the device
        dev = Device(host=device_info['host'], user=device_info['user'], password=device_info['password'])
        dev.open()

        # Fetch the configuration in set format
        config_set_format = dev.rpc.get_config(options={'format': 'set'})

        # File name based on the host (IP or hostname)
        filename = f"{device_info['host']}_config.set"

        # Write configuration to the file
        with open(filename, 'w', encoding="utf8") as config_file:
            config_file.write(config_set_format.text)

        print(f"Configuration saved for {device_info['host']} in {filename}")

    except ConnectError as err:
        print(f"Failed to connect to {device_info['host']}: {err}")
    
    finally:
        # Ensure the connection is closed
        dev.close()

# Loop through each device and fetch its configuration
for device_info in devices:
    fetch_config(device_info)
