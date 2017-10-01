#!/bin/bash

/usr/bin/python /home/pi/madmug/madmugbot.py > madmugbot.log &
/usr/bin/python /home/pi/madmug/buttoncontrol.py > buttoncontrol.log &

