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


parser1 = argparse.ArgumentParser(add_help=False)
parser1.add_argument("-h", "--help", default=False, action="store_true")
parser1.add_argument("-c", "--clear", default=False, action="store_true")
args1 = parser1.parse_known_args()

if(args1[0].help):
    print(msg())
    sys.exit(0)

if(args1[0].clear):
    os.system("sudo iptables -F INPUT")
    sys.exit(0)

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("ip", help="IP address to use")
group = parser.add_mutually_exclusive_group()
group.add_argument("-b", "--blkip", action="store_true", help="Specifies to block IP")
group.add_argument("-a", "--allowip", action="store_true", help="Specifies to allow IP")
parser.add_argument("-s", "--blkssh", action="store_true", help="Blocks ssh connections from a specific IP")
args = parser.parse_args()

try:
    socket.inet_aton(args.ip)
except socket.error:
    print("IP address was not valid, please enter a valid ip address")
    parser.print_help()
    sys.exit(0)

if(not args.blkip and not args.allowip and not args.blkssh):
    print("Please enter at least one optional argument")
    parser.print_help()
    sys.exit(0)

if(args.blkip and args.blkssh):
    os.system("sudo iptables -A INPUT -p tcp --dport ssh -s {} -j DROP".format(args.ip))
elif(args.allowip and args.blkssh):
    os.system("sudo iptables -A INPUT -p tcp --dport ssh -s {} -j ACCEPT".format(args.ip))
elif(args.blkip):
    os.system("sudo iptables -A INPUT -s {} -j DROP".format(args.ip))
elif(args.allowip):
    os.system("sudo iptables -A INPUT -s {} -j ACCEPT".format(args.ip))
elif(args.blkssh and not args.blkip and not args.allowip):
    os.system("sudo iptables -A INPUT -p tcp --dport ssh -j DROP")
else:
    parser.print_help()
