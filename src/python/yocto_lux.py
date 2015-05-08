#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os,sys

sys.path.append(os.path.join("..","..","lib","Yocto_light_meter"))
from yocto_api import *
from yocto_lightsensor import *

def usage():
    scriptname = os.path.basename(sys.argv[0])
    print("Usage:")
    print(scriptname+' <serial_number>')
    print(scriptname+' <logical_name>')
    print(scriptname+' any  ')
    sys.exit()

def die(msg):
    sys.exit(msg+' (check USB cable)')

errmsg=YRefParam()

target='LIGHTMK3-36011'

# Setup the API to use local USB devices
if YAPI.RegisterHub("usb", errmsg)!= YAPI.SUCCESS:
    sys.exit("init error"+errmsg.value)

if target=='any':
    # retreive any Light sensor
    sensor = YLightSensor.FirstLightSensor()
    if sensor is None :
        die('No module connected')
else:
    sensor= YLightSensor.FindLightSensor(target + '.lightSensor')

if not(sensor.isOnline()):die('device not connected')

while True:
    print("Light :  "+ str(int(sensor.get_currentValue()))+" lx (Ctrl-C to stop)")
    YAPI.Sleep(1000)
