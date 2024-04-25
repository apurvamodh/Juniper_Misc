from jnpr.junos import Device
from jnpr.junos.utils.scp import SCP

device = Device('10.85.153.10')

with SCP(device, progress=True) as scp:
    scp.put('/home/lab/jinstall-ppc-22.1.tgz', remote_path='/var/tmp/')
    scp.get('/var/log/messages', local_path='/home/lab')
