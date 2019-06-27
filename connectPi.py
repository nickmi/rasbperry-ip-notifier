#!/usr/bin/python3

##################################################
## Author: nickmi
## Copyright: Copyright 2019, raspberryIpNotifier
## License: GNU GPLv3
## Mmaintainer: nickmi
## Email: nikolasmichalaros@gmail.com
##################################################

import fabric
c = fabric.Connection("192.168.10.9", port=22, user="pi", connect_kwargs={'password': 'raspberry'})


def create_directories(c):
    c.run('mkdir /home/pi/BroadcastIP')


def upload_files(c):
    c.put('getIP.py','/home/pi/BroadcastIP')
    c.put('getIP.service','/home/pi/BroadcastIP')


def move_files(c):
    c.run('sudo mv /home/pi/BroadcastIP/getIP.service /lib/systemd/system/')


def enable_systemd_service(c):
    c.run('sudo systemctl start getIP.service')
    c.run('sudo systemctl enable getIP.service')


create_directories(c)
upload_files(c)
move_files(c)
enable_systemd_service(c)





