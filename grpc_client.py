import os
import json
 
from pygnmi.client import gNMIclient, telemetryParser
 
# Variables
hosts = [
    {
        "ip": "192.168.1.1",
        "port": 10162
    },
]
 
subscribe = {
    'subscription': [
        {
            'path': '/components',
            'mode': 'sample',
            'sample_interval': 10000000000
        }
    ],
    'mode': 'stream',
    'encoding': 'json'
}
 
for host in hosts:
    with gNMIclient(target=(host["ip"], host["port"]), username='root', password='Juniper',
            insecure=True, debug=True, no_qos_marking=True) as gc:
            telemetry_stream = gc.subscribe(subscribe=subscribe)
            for telemetry_entry in telemetry_stream:
                print(telemetryParser(telemetry_entry))
