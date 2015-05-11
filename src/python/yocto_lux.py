#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os,sys
#The path to the library
sys.path.append(os.path.join("..","..","lib","Yocto_light_meter"))
from yocto_api import *
from yocto_lightsensor import *

class Yocto():
    """docstring for Yocto"""
    def __init__(self):
        errmsg = YRefParam()
        target = 'LIGHTMK3-36011'
        if YAPI.RegisterHub("usb", errmsg)!= YAPI.SUCCESS:
            raise EnvironmentError("init error"+errmsg.value)
        self.sensor= YLightSensor.FindLightSensor(target + '.lightSensor')
        if self.sensor is None or not self.sensor.isOnline():
            print("connection failed")
            raise EnvironmentError("No Yocto sensor detected")

    def get_value(self):
        return int(self.sensor.get_currentValue())

