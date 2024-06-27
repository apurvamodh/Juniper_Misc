# This example code will use filters to extract a particular config stanza and the use of json to match on relavent parts
# Empty data will error out, exception handling is not done.

#!/usr/bin/python

from jnpr.junos import Device
from pprint import pprint
from lxml import etree

def main():
	filter_xml = etree.Element("configuration")
	interfaces = etree.SubElement(filter_xml, "interfaces")
	
	with Device("10.85.168.50", user="root", passwd="Juniper") as dev:
		config_data = dev.rpc.get_config(filter_xml=filter_xml, options={"format": "json"})

		print("Configured Interfaces:")
		for interface in config_data["configuration"]["interfaces"]["interface"]:
			print(interface["name"])

if __name__ == "__main__":
    main()