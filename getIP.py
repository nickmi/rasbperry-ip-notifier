#!/usr/bin/python3

##################################################
## Author: nickmi
## Copyright: Copyright 2019, raspberryIpNotifier
## License: GNU GPLv3
## Mmaintainer: nickmi
## Email: nikolasmichalaros@gmail.com
##################################################

import netifaces as ni
import paho.mqtt.publish as publish

def getIP():
    try:
        return ni.ifaddresses('eth0')[ni.AF_INET][0]['addr'] + " My name is raspbery pi {ID}"
    except:
        print("Failed to get address")

def publishIP():
    topic = "{TOPIC}"
    publish.single(topic, ip, qos=0, retain=False, hostname="broker.mqttdashboard.com",
    port=1883, client_id="", keepalive=60, will=None, auth=None, tls=None,transport="tcp")

ip = getIP()
publishIP(ip)

