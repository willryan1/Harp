import os
from . import Device

def help():
    print("Core Commands\n==============\nCommand       Description\n-------       -----------\ninstall       Install dependencies\nstart         Start routing\nstop          Stop routing\nrestart       Restart the process\nstatus        See status\n\n")

def install():
    operatingSystem = Device.getSystem()
    
    os.system("sudo mkdir -p /etc/tor")

    if(operatingSystem == "debian"):
        os.system ("sudo apt-get install tor iptables");
        os.system ("sudo cp .configs/debian-torrc /etc/tor/torrc");
    elif(operatingSystem == "arch"):
        os.system ("sudo pacman -S tor iptables");
        os.system ("sudo cp .configs/arch-torrc /etc/tor/torrc");
    elif(operatingSystem == "fedora"):
        os.system ("sudo dnf install tor iptables");
        os.system ("sudo cp .configs/fedora-torrc /etc/tor/torrc");
    elif(operatingSystem == "centos"):
        os.system ("sudo yum install epel-release tor iptables");
        os.system ("sudo cp .configs/centos-torrc /etc/tor/torrc");
    else:
        os.system ("sudo pacman -S tor iptables");
        os.system ("sudo cp .configs/arch-torrc /etc/tor/torrc");
    
    os.system ("sudo chmod 644 /etc/tor/torrc");

