import os

def new():
    os.system("sudo iptables -F INPUT")
    os.system("sudo iptables -A INPUT -i lo -j ACCEPT")
    os.system("sudo iptables -A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT")
    os.system("sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT")
    os.system("sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT")
    os.system("sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT")
    os.system("sudo iptables -A INPUT -j DROP")

def new_secure():
    os.system("sudo iptables -F INPUT")
    os.system("sudo iptables -A INPUT -i lo -j ACCEPT")
    os.system("sudo iptables -A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT")
    os.system("sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT")
    os.system("sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT")
    os.system("sudo iptables -A INPUT -j DROP")

