from jnpr.junos import Device
from jnpr.junos.utils.start_shell import StartShell

dev = Device('10.85.153.10')

ss = StartShell(dev)

ss.open()

software_image = ss.run('ls -al /var/tmp/jinstall*')
print(software_image[1])

command = ss.run('cli -c "show system storage"')
print(command)

ss.close()
