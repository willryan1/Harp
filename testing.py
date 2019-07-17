import argparse
import os
import sys
import socket

def msg():
    return """usage: block_ip.py [-h | -c] [-b | -a] [-s] ip

Block and allow certain IP adresses

positional arguments:
  ip             IP address to use

optional arguments:
  -h, --help     show this help message and exit
  -c  --clear    sets the input in iptables back to the default settings
  -b, --blkip    specifies to block IP
  -a, --allowip  specifies to allow IP
  -s, --blkssh   Blocks ssh connections from a specific IP"""


parser = argparse.ArgumentParser()
parser.add_argument("-h", "--help", default=False, action="store_true", help="Displays help message")
parser.add_argument("-c", "--clear", default=False, action="store_true", help="Clears all settings")
parser.add_argument("-i", "--ip", nargs=2, help="Block or allow a certain ip **Usage: -i (block | block+ | allow) ip**")
parser.add_argument('-s', '--start', default=False, action='store_true', help="Starts the firewall")
parser.add_argument('-h', '--halt', default=False, action='store_true', help="Halts the firewall")
args = parser.parse_args()

if(args[0].help):
    print(msg())
    sys.exit(0)

if(args[0].clear):
    os.system("sudo iptables -F INPUT")
    sys.exit(0)

if(args[0].ip is not None):
    try:
        socket.inet_aton(args[0].ip[1])
    except socket.error:
        print("IP address was not valid, please enter a valid ip address")
        msg()
        sys.exit(0)
    if(args[0].ip[0] == "block+"):
        os.system("sudo iptables -A INPUT -p tcp --dport ssh -s {} -j DROP".format(args[0].ip[1]))
    elif(args[0].ip[0] == "block"):
        os.system("sudo iptables -A INPUT -s {} -j DROP".format(args[0].ip[1]))
    elif(args[0].ip[0] == "allow"):
        os.system("sudo iptables -A INPUT -s {} -j ACCEPT".format(args[0].ip[1]))
    else:
        print("You entered something wrong")
        msg()
        sys.exit()


