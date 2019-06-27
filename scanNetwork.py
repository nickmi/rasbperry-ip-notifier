#!/usr/bin/python3

##################################################
## Author: nickmi
## Copyright: Copyright 2019, raspberryIpNotifier
## License: GNU GPLv3
## Mmaintainer: nickmi
## Email: nikolasmichalaros@gmail.com
##################################################

import subprocess


def get_nmap(options, ip):
    return subprocess.check_output(["nmap", options, ip])


print(get_nmap('-sn','192.168.10.0/24'))