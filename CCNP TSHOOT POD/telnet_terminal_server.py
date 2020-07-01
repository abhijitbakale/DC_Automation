import telnetlib

tn = telnetlib.Telnet(host="192.100.101.201")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("conf t\n")

for i in range(41, 47):
  tn.write("do clear line " + str(i) + "\n\n")

tn.write("end\n")
tn.write("exit\n")

print tn.read_all()
