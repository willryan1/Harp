import os
from os import path

def new():
    tables = ["nat", "filter"]

    for table in tables:
        
        os.system ("sudo iptables -t {} -F OUTPUT".format(table))
        os.system ("sudo iptables -t {} -F OUTPUT".format(table))

    if(path.exists("/etc/init.d/tor")):
        os.system ("sudo /etc/init.d/tor stop > /dev/null");
    else:
        os.system ("sudo systemctl stop tor")

    return True
