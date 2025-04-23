# Example of a nested dictionary structure for network devices
network_devices = {
    "router1": {
        "hostname": "core-router-1",
        "model": "Cisco ASR 9000",
        "location": "Data Center A",
        "interfaces": {
            "GigabitEthernet0/0/0": {
                "ip_address": "192.168.1.1",
                "subnet_mask": "255.255.255.0",
                "mtu": 1500,
                "status": "up",
                "speed": "1Gbps",
                "duplex": "full"
            },
            "GigabitEthernet0/0/1": {
                "ip_address": "10.0.0.1",
                "subnet_mask": "255.255.255.0",
                "mtu": 9000,
                "status": "up",
                "speed": "1Gbps",
                "duplex": "full"
            },
            "TenGigE0/1/0": {
                "ip_address": "172.16.0.1",
                "subnet_mask": "255.255.255.0",
                "mtu": 9000,
                "status": "up",
                "speed": "10Gbps",
                "duplex": "full"
            }
        },
        "hardware": {
            "cpu": {
                "model": "Intel Xeon",
                "cores": 16,
                "speed": "2.6 GHz"
            },
            "memory": {
                "total": "64GB",
                "type": "DDR4",
                "speed": "2666 MHz"
            },
            "storage": {
                "type": "SSD",
                "capacity": "512GB",
                "free_space": "350GB"
            }
        }
    },
    "switch1": {
        "hostname": "access-switch-1",
        "model": "Arista DCS-7280",
        "location": "Data Center B",
        "interfaces": {
            "Ethernet1": {
                "ip_address": "192.168.2.1",
                "subnet_mask": "255.255.255.0",
                "mtu": 1500,
                "status": "up",
                "speed": "1Gbps",
                "duplex": "full"
            },
            "Ethernet2": {
                "ip_address": "10.0.1.1",
                "subnet_mask": "255.255.255.0",
                "mtu": 1500,
                "status": "down",
                "speed": "1Gbps",
                "duplex": "full"
            },
            "Ethernet3/1": {
                "ip_address": None,  # Trunk port with no IP
                "vlan": 10,
                "mtu": 9000,
                "status": "up",
                "speed": "10Gbps",
                "duplex": "full"
            }
        },
        "hardware": {
            "cpu": {
                "model": "AMD EPYC",
                "cores": 8,
                "speed": "3.2 GHz"
            },
            "memory": {
                "total": "32GB",
                "type": "DDR4",
                "speed": "3200 MHz"
            },
            "power_supplies": {
                "total": 2,
                "redundant": True,
                "active": [1],
                "standby": [2]
            }
        }
    },
    "firewall1": {
        "hostname": "edge-fw-1",
        "model": "Palo Alto PA-5250",
        "location": "Data Center A",
        "interfaces": {
            "ethernet1/1": {
                "ip_address": "203.0.113.1",
                "subnet_mask": "255.255.255.0",
                "mtu": 1500,
                "status": "up",
                "zone": "untrust",
                "speed": "10Gbps"
            },
            "ethernet1/2": {
                "ip_address": "10.100.0.1",
                "subnet_mask": "255.255.255.0",
                "mtu": 1500,
                "status": "up",
                "zone": "trust",
                "speed": "10Gbps"
            }
        },
        "hardware": {
            "cpu": {
                "model": "Custom Security Processor",
                "cores": 4,
                "utilization": "23%"
            },
            "memory": {
                "total": "16GB",
                "utilization": "45%"
            },
            "storage": {
                "type": "SSD",
                "capacity": "256GB",
                "log_storage": "128GB"
            },
            "throughput": {
                "max": "20Gbps",
                "current": "5.2Gbps"
            }
        },
        "security_policies": {
            "policy1": {
                "source": "any",
                "destination": "10.100.0.0/24",
                "service": "http",
                "action": "allow",
                "logging": True
            },
            "policy2": {
                "source": "10.100.0.0/24",
                "destination": "any",
                "service": "any",
                "action": "allow",
                "logging": True
            }
        }
    }
}

# Example of accessing data in the nested dictionary
print(f"Router1 model: {network_devices['router1']['model']}")
print(f"Switch1 Ethernet1 IP: {network_devices['switch1']['interfaces']['Ethernet1']['ip_address']}")
print(f"Firewall1 Security Policy1 action: {network_devices['firewall1']['security_policies']['policy1']['action']}")

# Iterating through all devices
for device_name, device_data in network_devices.items():
    print(f"\nDevice: {device_name} ({device_data['hostname']})")
    
    # Print all interfaces for each device
    print("Interfaces:")
    for interface_name, interface_data in device_data['interfaces'].items():
        status = interface_data['status']
        ip = interface_data.get('ip_address', 'N/A')
        print(f"  - {interface_name}: {ip} ({status})")
    
    # Print hardware components
    print("Hardware:")
    for component, specs in device_data['hardware'].items():
        if isinstance(specs, dict):
            comp_details = ", ".join([f"{k}: {v}" for k, v in specs.items() if k in ['model', 'total', 'type']])
            print(f"  - {component}: {comp_details}")