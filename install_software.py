# This example uses Juniper PyEZ SW library to install software on the device.
# Folloing tasks are performed during the install:
# 1. Compute checksum of the new sw image
# 2. Perform storage cleanup on device
# 3. Copy sw image to the target device and re-compute checksum 
# 4. Validate the current device configuration against the new sw image
# 5. Install junos on the target device

import sys
from jnpr.junos import Device
from jnpr.junos.utils.sw import SW
from jnpr.junos.exception import ConnectError, SW_Error

def upgrade_junos_device(host, username, password, image_path):
    """
    Upgrade a Junos device using PyEZ library
    
    :param host: IP address or hostname of the Junos device
    :param username: Login username
    :param password: Login password
    :param image_path: Path to the Junos image file
    """
    try:
        # Establish connection to the Junos device
        print(f"Connecting to device: {host}")
        dev = Device(host=host, user=username, password=password)
        dev.open()
        
        # Create a Software Upgrade utility instance
        sw = SW(dev)
        
        # Check if the image is already present on the device
        print(f"Checking if image exists: {image_path}")
        if not sw.validate(image_path):
            print(f"Transferring image {image_path} to the device...")
            # Transfer the software image to the device
            sw.put(image_path)
        
        # Perform pre-upgrade checks
        print("Performing pre-upgrade validation...")
        sw.validate(image_path)
        
        # Install the image
        print(f"Installing image: {image_path}")
        sw.install(image_path)
        
        # Request the device to reboot
        print("Rebooting the device...")
        sw.reboot()
        
        # Close the connection
        dev.close()
        
        print("Upgrade process initiated successfully!")
    
    except ConnectError as err:
        print(f"Connection Error: {err}")
        sys.exit(1)
    except SW_Error as err:
        print(f"Software Upgrade Error: {err}")
        sys.exit(1)
    except Exception as err:
        print(f"Unexpected error occurred: {err}")
        sys.exit(1)

def main():
    # Example usage
    host = '192.168.1.1'  # Replace with your device's IP
    username = 'admin'    # Replace with your username
    password = 'password' # Replace with your password
    image_path = '/path/to/junos-image.tgz'  # Replace with actual image path
    
    upgrade_junos_device(host, username, password, image_path)

if __name__ == '__main__':
    main()