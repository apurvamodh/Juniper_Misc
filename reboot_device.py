from jnpr.junos import Device
from jnpr.junos.utils.sw import SW

with Device('10.85.153.10') as dev:
    sw = SW(dev)
    print(sw.poweroff(in_min='5'))
    # OR
    # print(sw.reboot(at='23:55'))
