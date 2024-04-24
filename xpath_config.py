#! usr/bin/python3

# Usage
# python3 xpath_config.py 
# python3 xpath_config.py system/services
# python3 xpath_config.py ./@changed-localtime
# python3 xpath_config.py system/login/user/id
# python3 xpath_config.py "system/login/user[name='admin']/id"
# python3 xpath_config.py 'interfaces/interface[starts-with(name, "ge")]'
# python3 xpath_config.py 'interfaces/interface[name="lo0" or name="fxp0"]'

from jnpr.junos import Device
from lxml.tree import dump, _Element
from sys import argv

# Use the provided value as the xpath regex to filter the config or use
# "." if no args are provided. 
conf_xpath = argv[1] if len(argv) > 1 else "."

# device management ip
device = "10.85.153.83"

# Open a netconf connection to the device using Juniper PyEz device object
with Device(host=device) as dev:
	# Retrieve complete device config using <get-config> RPC
	full_config = dev.rpc.get_config()

	# Filter the config using xpath
	filtered_config = full_config.xpath(conf_xpath)

	# Perform a loop against the returned Xpath filtered results 
	for entry in filtered_config:
		# for each entry print it out using dump() or print()
		if type(entry) is _Element:
			dump(entry)
		else:
			print(entry)
					

