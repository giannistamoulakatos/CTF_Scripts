import os 

ser_in = input("What you want interface change ? = ")
down = os.system(f'sudo ip link set dev {ser_in} down')
mac_ran_w = os.system(f'macchanger -r {ser_in}')
up = os.system(f'sudo ip link set dev {ser_in} up')
