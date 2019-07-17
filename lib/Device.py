import os

id_str = "ID_LIKE"

OS = ''

with open(os.path.expanduser("/etc/os-release"), 'r') as f:
    for line in f:
        if(id_str in line):
            OS = line
            break
OS = OS[8:].rstrip().lower()

def getUsername():
    username = ''
    if(OS == "ubuntu" or OS == "arch"):
        username = "tor"
    elif(OS == "debian"):
        username = "debian-tor"
    elif(OS == "fedora" or OS == "centos"):
        username = "toranon"
    else:
        username = "tor"
    return username

def getSystem():
    distribution = ''
    if(OS == "ubuntu" or OS == "debian"):
        distribution = "debian"
    elif(OS == "fedora"):
        distribution = "fedora"
    elif(OS == "arch"):
        distribution = "arch"
    elif(OS == "centos"):
        distribution = "centos"
    else:
        distribution = "debian"
    return distribution

