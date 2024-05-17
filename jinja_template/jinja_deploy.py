from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import yaml

junos_hosts = ['vmx-1', 'vmx-2']

for host in junos_hosts:
    file_name = host + '.yml'
    with open(file_name, 'r') as fh:
        data = yaml.safe_load(fh)
        with Device(host) as dev:
            with Config(dev, mode="exclusive") as conf:
                conf.load(template_path="example.j2", template_vars=data, format="text")
                conf.pdiff()
                conf.commit()
            print("Configuration loaded successfully")
