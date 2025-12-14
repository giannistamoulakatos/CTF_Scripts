import os
import subprocess as sb

ip=input("Give the ip address = ")
np_command=os.system(f"nmap {ip} -p- -T5 -sC -oN results.txt")
r_file = os.popen("grep open results.txt |grep -E 'tcp|http|ssh'").read()
ports = []
for line in r_file.splitlines():
    port = line.split("/")[0]   
    ports.append(port)

portsfinal = ",".join(ports)
np2=os.system(f"nmap {ip} -sV -p{portsfinal} -oN ports.txt")
serv=[]
with open("ports.txt","r") as dp:
    for line in dp:
        if "open" in line and "/" in line:
            partsV = line.split()
            if len(partsV) >= 3:
                ser = partsV[2]                    
                serv.append(ser)
for sv in serv:
    rs = sb.run(['searchsploit',sv] , capture_output = True, text = True)
    results = rs.stdout
    print(results)

    

