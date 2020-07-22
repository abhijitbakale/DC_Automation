from netmiko import ConnectHandler

Tshoot_ASW2 = {
    'device_type': 'cisco_ios',
    'ip':'192.100.101.201',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco',
    'port':2038,
    'global_delay_factor':5
}

with open('C:\Users\user1\Desktop\DC_Automation_Scripts\Tshoot_Pod_Config\ASW2.txt') as f:
    lines = f.read().splitlines()
print lines

net_connect = ConnectHandler(**Tshoot_ASW2)
net_connect.enable()
print net_connect.find_prompt()
print "Sesion Estabilished with Tshoot_ASW2"

output = net_connect.send_config_set(config_commands=lines, max_loops=10000, delay_factor=5)
print output