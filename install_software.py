# This example uses Juniper PyEZ SW library to install software on the device.
# Folloing tasks are performed during the install:
# 1. Compute checksum of the new sw image
# 2. Perform storage cleanup on device
# 3. Copy sw image to the target device and re-compute checksum 
# 4. Validate the current device configuration against the new sw image
# 5. Install junos on the target device


from jnpr.junos import Device
from jnpr.junos.utils.sw import SW

pkg = "jinstall-ppc-21.1R1.tgz"

with Device('10.85.153.10') as dev:
    sw = SW(dev)
    ok, msg = sw.install(package=pkg, validate=True, checksum_algorithm='sha256')
    print("Status: " + str(ok) + ", Message: ", msg)
    if ok:
        sw.reboot()
