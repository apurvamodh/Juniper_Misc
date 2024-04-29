from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import sys

try:
    with Device(host='10.85.153.10') as dev:
        with Config(dev, mode="exclusive") as cu:
            rescue = cu.rescue(action="reload")
            if rescue:
                cu.commit()
                print("Rescue configuration successfully loaded")
            else:
                print("No rescue configuration exists")

except Exception as err:
    print (err)
    sys.exit(1)