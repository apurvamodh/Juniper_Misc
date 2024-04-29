from jnpr.junos import Device
from jnpr.junos.utils.config import Config

dev = Device(host='10.85.153.10')
dev.open()
conf = Config(dev)
data = """interfaces {
    ge-0/0/2 {
        unit 0 {
            family inet {
                address 172.17.1.15/24;
            }
        }
    }
}"""

# for the set option to load config use following,
# data_set = 'set system services netconf traceoptions file test.log'

conf.lock()
conf.load(data, format='text') # conf.load(data_set, format='set')
conf.pdiff()

if conf.commit_check():
    conf.commit()
else:
    conf.rollback()

conf.unlock()
dev.close()
