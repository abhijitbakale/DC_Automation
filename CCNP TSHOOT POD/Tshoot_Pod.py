from netmiko import ConnectHandler
import pod_info

tshoot_pod = [pod_info.Tshoot_R1, 
pod_info.Tshoot_R2, pod_info.Tshoot_R3, pod_info.Tshoot_R4, pod_info.Tshoot_FR_SW, pod_info.Tshoot_ISP,
pod_info.Tshoot_DSW1,pod_info.Tshoot_DSW2,pod_info.Tshoot_ASW1,pod_info.Tshoot_ASW2]
for devices in tshoot_pod: 
    
    if devices ==  tshoot_pod[0]:
        with open('C:\Users\user1\Desktop\DC_Automation_Scripts\Tshoot_Pod_Config\R1.txt') as f:
            lines = f.read().splitlines()

        net_connect = ConnectHandler(**devices)
        net_connect.enable()
        print net_connect.find_prompt()
        print "Sesion Estabilished with Tshoot_R1"
        print "Establishing Connection with " + str(devices["ip"]) + ":" + str(devices["port"])
        output = net_connect.send_config_set(config_commands=lines, max_loops=10000, delay_factor=5)
        print output

    if devices ==  tshoot_pod[1]:
        with open('C:\Users\user1\Desktop\DC_Automation_Scripts\Tshoot_Pod_Config\R2.txt') as f:
            lines = f.read().splitlines()

        net_connect = ConnectHandler(**devices)
        net_connect.enable()
        print net_connect.find_prompt()
        print "Sesion Estabilished with Tshoot_R2"
        print "Establishing Connection with " + str(devices["ip"]) + ":" + str(devices["port"])
        output = net_connect.send_config_set(config_commands=lines, max_loops=10000, delay_factor=5)
        print output
    
    if devices ==  tshoot_pod[2]:
        with open('C:\Users\user1\Desktop\DC_Automation_Scripts\Tshoot_Pod_Config\R3.txt') as f:
            lines = f.read().splitlines()

        net_connect = ConnectHandler(**devices)
        net_connect.enable()
        print net_connect.find_prompt()
        print "Sesion Estabilished with Tshoot_R3"
        print "Establishing Connection with " + str(devices["ip"]) + ":" + str(devices["port"])
        output = net_connect.send_config_set(config_commands=lines, max_loops=10000, delay_factor=5)
        print output
    
    if devices ==  tshoot_pod[3]:
        with open('C:\Users\user1\Desktop\DC_Automation_Scripts\Tshoot_Pod_Config\R4.txt') as f:
            lines = f.read().splitlines()

        net_connect = ConnectHandler(**devices)
        net_connect.enable()
        print net_connect.find_prompt()
        print "Sesion Estabilished with Tshoot_R4"
        print "Establishing Connection with " + str(devices["ip"]) + ":" + str(devices["port"])
        output = net_connect.send_config_set(config_commands=lines, max_loops=10000, delay_factor=5)
        print output
    
    if devices ==  tshoot_pod[4]:
        with open('C:\Users\user1\Desktop\DC_Automation_Scripts\Tshoot_Pod_Config\FR-SW.txt') as f:
            lines = f.read().splitlines()

        net_connect = ConnectHandler(**devices)
        net_connect.enable()
        print net_connect.find_prompt()
        print "Sesion Estabilished with Tshoot_FR-SW"
        print "Establishing Connection with " + str(devices["ip"]) + ":" + str(devices["port"])
        output = net_connect.send_config_set(config_commands=lines, max_loops=10000, delay_factor=5)
        print output

    if devices ==  tshoot_pod[5]:
        with open('C:\Users\user1\Desktop\DC_Automation_Scripts\Tshoot_Pod_Config\ISP.txt') as f:
            lines = f.read().splitlines()

        net_connect = ConnectHandler(**devices)
        net_connect.enable()
        print net_connect.find_prompt()
        print "Sesion Estabilished with Tshoot_ISP"
        print "Establishing Connection with " + str(devices["ip"]) + ":" + str(devices["port"])
        output = net_connect.send_config_set(config_commands=lines, max_loops=10000, delay_factor=5)
        print output

    if devices ==  tshoot_pod[6]:
        with open('C:\Users\user1\Desktop\DC_Automation_Scripts\Tshoot_Pod_Config\DSW1.txt') as f:
            lines = f.read().splitlines()

        net_connect = ConnectHandler(**devices)
        net_connect.enable()
        print net_connect.find_prompt()
        print "Sesion Estabilished with Tshoot_DSW1"
        print "Establishing Connection with " + str(devices["ip"]) + ":" + str(devices["port"])
        output = net_connect.send_config_set(config_commands=lines, max_loops=10000, delay_factor=5)
        print output
    
    if devices ==  tshoot_pod[7]:
        with open('C:\Users\user1\Desktop\DC_Automation_Scripts\Tshoot_Pod_Config\DSW2.txt') as f:
            lines = f.read().splitlines()

        net_connect = ConnectHandler(**devices)
        net_connect.enable()
        print net_connect.find_prompt()
        print "Sesion Estabilished with Tshoot_DSW2"
        print "Establishing Connection with " + str(devices["ip"]) + ":" + str(devices["port"])
        output = net_connect.send_config_set(config_commands=lines, max_loops=10000, delay_factor=5)
        print output

    if devices ==  tshoot_pod[8]:
        with open('C:\Users\user1\Desktop\DC_Automation_Scripts\Tshoot_Pod_Config\ASW1.txt') as f:
            lines = f.read().splitlines()

        net_connect = ConnectHandler(**devices)
        net_connect.enable()
        print net_connect.find_prompt()
        print "Sesion Estabilished with Tshoot_ASW1"
        print "Establishing Connection with " + str(devices["ip"]) + ":" + str(devices["port"])
        output = net_connect.send_config_set(config_commands=lines, max_loops=10000, delay_factor=5)
        print output

    if devices ==  tshoot_pod[9]:
        with open('C:\Users\user1\Desktop\DC_Automation_Scripts\Tshoot_Pod_Config\ASW2.txt') as f:
            lines = f.read().splitlines()

        net_connect = ConnectHandler(**devices)
        net_connect.enable()
        print net_connect.find_prompt()
        print "Sesion Estabilished with Tshoot_ASW2"
        print "Establishing Connection with " + str(devices["ip"]) + ":" + str(devices["port"])
        output = net_connect.send_config_set(config_commands=lines, max_loops=10000, delay_factor=5)
        print output

    # net_connect = ConnectHandler(**devices)
    # net_connect.enable()
    # net_connect.find_prompt()

    #print "Establishing Connection with " + str(devices["ip"]) + ":" + str(devices["port"])


    #output = net_connect.send_command('show ip interface brief')
    #print output
    