from . import Device
import os
from os import path

def new():
    dns_port = "9061"
    transfer_port = "9051"
    tables = ["nat", "filter"]
    network = "10.66.0.0/255.255.0.0"

    username  = Device.getUsername()
    
    if(path.exists("/etc/init.d/tor")):
        os.system("sudo /etc/init.d/tor start > /dev/null")
    else:
        os.system("sudo systemctl start tor") # could need to be fixed for mac implementation
    
    for table in tables:
        target = "ACCEPT"

        if(table == "nat"):
            target = "RETURN"
        
        os.system("sudo iptables -t {} -F OUTPUT".format(table))
        os.system("sudo iptables -t {} -A OUTPUT -m state --state ESTABLISHED -j {}".format(table, target))
        os.system("sudo iptables -t {} -A OUTPUT -m owner --uid {} -j {}".format(table, username, target))

        match_dns_port = dns_port

        if(table == "nat"):
            target = "REDIRECT --to-ports {}".format(dns_port)
            match_dns_port = "53"

        os.system("sudo iptables -t {} -A OUTPUT -p udp --dport {} -j {}".format(table, match_dns_port, target))
        os.system("sudo iptables -t {} -A OUTPUT -p tcp --dport {} -j {}".format(table, match_dns_port, target))

        if(table == "nat"):
            target = "REDIRECT --to-ports {}".format(transfer_port)

        os.system("sudo iptables -t {} -A OUTPUT -d {} -p tcp -j {}".format(table, network, target))

        if(table == "nat"):
            target = "RETURN"

        os.system ("sudo iptables -t {} -A OUTPUT -d 127.0.0.1/8    -j {}".format(table, target))
        os.system ("sudo iptables -t {} -A OUTPUT -d 192.168.0.0/16 -j {}".format(table, target))
        os.system ("sudo iptables -t {} -A OUTPUT -d 172.16.0.0/12  -j {}".format(table, target))
        os.system ("sudo iptables -t {} -A OUTPUT -d 10.0.0.0/8     -j {}".format(table, target))
        
        if(table == "nat"):
            target = "REDIRECT --to-ports {}".format(transfer_port)

            
        os.system ("sudo iptables -t {} -A OUTPUT -p tcp -j {}".format(table, target))

    os.system ("sudo iptables -t filter -A OUTPUT -p udp -j REJECT")
    os.system ("sudo iptables -t filter -A OUTPUT -p icmp -j REJECT")

    return True

