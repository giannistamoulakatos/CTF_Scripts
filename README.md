# CTF_Scripts

This is scripts that make for capture the flag challenges. We have three scripts. One Script with NMAP and searchsploit tool. Second script it use binwalk for decrypt images and the last script use a macchanger tool for change a mac address

## NMAP Searchsloit Script

First insert the ip address in the script. The ip address is address for another machine. the script it first shows the ports and next the shows services where can attack the machine. The results is saving in the txt files in one txt there are the ports from machine and the another txt file there are services from machine. In addition in the next part shows the exploits with searchsploit. the exploits is exploits for services of the machine.

## Reverse Enginiring Binwalk
In this script we insert one image and next with binwalk tool we take a bytes from images and the signature from image. The script saves the results in two txt files. In one file save the bytes and the another file save the signature of image.

## Macchanger
In this script it run service LAN or WLAN and give us a random MAC address with macchanger tool.
