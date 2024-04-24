# Python 3
from jnpr.junos import Device
from getpass import getpass
from lxml import etree
from jnpr.junos.utils.config import Config
import sys

hostname = "10.85.155.240"
junos_username = "lab"
junos_password = "lab123"

try: 
    # NETCONF session over SSH
    with Device(host=hostname, user=junos_username, passwd=junos_password) as dev:
    
    # Telnet connection to device or console server connected to device
    #with Device(host=hostname, user=junos_username, passwd=junos_password, mode='telnet', port='23') as dev:

    # Serial console connection to device
    #with Device(host=hostname, user=junos_username, passwd=junos_password, mode='serial', port='/dev/ttyUSB0') as dev:

    # SSH connection to console server connected to device
    #with Device(host=hostname, user=junos_username, passwd=junos_password, cs_user=cs_username, cs_passwd=cs_password, timeout=5) as dev:

        # print (dev.facts)
        # time.sleep(5)

        # Login to device as conf exclusive
        with Config(dev, mode='exclusive') as cu:
            cu.load(path='/var/tmp/amodh.conf', merge=True)
            cu.pdiff()
            cu.commit()

        # show chassis firmware
        r1 = dev.rpc.get_firmware_information()
        print(etree.tostring(r1))


        # SNMP walk example.
        #<walk-snmp-object><ascii/><snmp-object-name>lldpRemPortId</snmp-object-name></walk-snmp-object>
        print(etree.tostring(dev.rpc.walk_snmp_object(snmp_object_name='lldpRemPortId')))

        # Fetch interface information
        # use this for all interfaces -> rsp = dev.rpc.get_interface_information()
        rsp = dev.rpc.get_interface_information(interface_name='ge-0/0/0')
        print(etree.tostring(rsp))
        print(etree.tostring(dev.rpc.get_interface_information(descriptions=True)))

except Exception as err:
    print (err)
    sys.exit(1)
