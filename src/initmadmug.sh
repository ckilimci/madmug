#!/bin/bash

/usr/bin/python /home/pi/madmug/madmugbot.py > /home/pi/madmug/madmugbot.log &
/usr/bin/python /home/pi/madmug/buttoncontrol.py > /home/pi/madmug/buttoncontrol.log &

