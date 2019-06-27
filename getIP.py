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
import json
CONST_RASPBERRYID = "40"


def get_network_info():
    try:
        return ni.ifaddresses('eno1')[ni.AF_INET][0]
    except:
        print("Failed to get address")


def publish_network_info(raspberry_info):
    topic = "ipTesterScript"
    publish.single(topic, raspberry_info, qos=0, retain=False, hostname="broker.mqttdashboard.com",
    port=1883, client_id="", keepalive=60, will=None, auth=None, tls=None,transport="tcp")


raspberry_info = get_network_info()
raspberry_info.update({'raspberryID':CONST_RASPBERRYID})
print(raspberry_info,"\nMy id is " + CONST_RASPBERRYID)
publish_network_info(json.dumps(raspberry_info))

