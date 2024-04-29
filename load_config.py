from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import sys

try:
    with Device(host='10.85.153.10') as dev:
        with Config(dev, mode="exclusive") as cu:
            cu.load(url="/var/home/ijaut/example.conf", overwrite=True)
            cu.commit()
            print("Device configuration loaded successfully")

except Exception as err:
    print (err)
    sys.exit(1)
