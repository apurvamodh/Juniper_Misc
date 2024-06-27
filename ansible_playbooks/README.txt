To execute ansible playbooks, we need to run ansible in the python vitual env.
For more details, watch this - https://www.youtube.com/watch?v=zhgZbaqL3Rk

=> Steps to activate python virtual env

python3.7 -m venv ansible-env
source ansible-env/bin/activate

to deactivate - type deactivate

example -
```
root@kinshukc-ubuntu16-vm1:~/amodh_scripts/ansible# 
root@kinshukc-ubuntu16-vm1:~/amodh_scripts/ansible# python3.7 --version
Python 3.7.12
root@kinshukc-ubuntu16-vm1:~/amodh_scripts/ansible# python3.7 -m venv ansible-env
root@kinshukc-ubuntu16-vm1:~/amodh_scripts/ansible# source ansible-env/bin/activate
(ansible-env) root@kinshukc-ubuntu16-vm1:~/amodh_scripts/ansible# 
```

pip install --upgrade pip
pip install ansible

--- below steps are taken from Juniper documentation (not tested)

pip3 install junos-eznc
pip3 install jxmlease
pip3 install ansible
ansible-galaxy install Juniper.junos

- Device needs to have netconf ssh enabled.
