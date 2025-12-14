import os 

down = os.system(f'sudo ip link set dev wlan0 down')
down2 = os.system(f'sudo ip link set dev eth0 down')
mac_ran_w = os.system(f'macchanger -r wlan0')
mac_ran_e = os.system(f'macchanger -r eth0')
