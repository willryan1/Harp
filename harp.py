from lib import Device
from lib import Functions
from lib import CheckIp
from lib import Start
from lib import Stop
from lib import input_config
from lib import clear_all_rules
import sys
import argparse
import os
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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--clear", default=False, action="store_true", help="Clears all settings")
    parser.add_argument("-i", "--ip", nargs=2, help="Block or allow a certain ip **Usage: -i (block | block+ | allow) ip**")
    parser.add_argument('-s', '--start', default=False, action='store_true', help="Starts the firewall")
    parser.add_argument('-d', '--download', default=False, action='store_true', help='downloads dependencies')
    parser.add_argument('-r', '--restart', default=False, action='store_true', help='restarts system')
    parser.add_argument('-p', '--printstatus', default=False, action='store_true', help='Prints status')
    args = parser.parse_args()


    if(args.ip is not None):
        try:
            socket.inet_aton(args.ip[1])
        except socket.error:
            print("IP address was not valid, please enter a valid ip address")
            args.print_help()
            sys.exit(0)
        if(args.ip[0] == "block+"):
            os.system("sudo iptables -A INPUT -p tcp --dport ssh -s {} -j DROP".format(args.ip[1]))
        elif(args.ip[0] == "block"):
            os.system("sudo iptables -A INPUT -s {} -j DROP".format(args.ip[1]))
        elif(args.ip[0] == "allow"):
            os.system("sudo iptables -A INPUT -s {} -j ACCEPT".format(args.ip[1]))
        else:
            print("You entered something wrong")
            args.print_help()
            sys.exit()
    elif(args.clear):
        Stop.new()
        clear_all_rules.new()
    elif(args.start):
        Start.new()
        input_config.new()
    elif(args.download):
        Functions.install()
    elif(args.restart):
        Stop.new()
        clear_all_rules.new()
        Start.new()
        input_config.new()
    elif(args.printstatus):
        CheckIp.new()
    else:
        args.print_help()

if __name__ == '__main__':
    main()

