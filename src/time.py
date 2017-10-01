#!/usr/bin/env python

import subprocess
import sys
import time

import scrollphat


scrollphat.set_brightness(2)

# Every refresh_interval seconds we'll refresh the uptime
# Only has to change every 60 seconds.
pause = 0.12
ticks_per_second = 1/pause
refresh_interval = 20

def get_timeout():
    return ticks_per_second * refresh_interval

def get_msg():
    val = subprocess.check_output(["date", "+%H:%M", "-d", "3 hours"]).decode("utf-8")
    val = val + "    "
    return val

timeout = get_timeout()
count = 0
msg = get_msg()
scrollphat.write_string(msg)

while True:
    try:
        scrollphat.scroll()
        time.sleep(pause)

        if(count > timeout):
            msg = get_msg()
            scrollphat.write_string(msg)
            timeout = get_timeout()
            count = 0
            print ("Updating uptime message")
        else:
            count = count+ 1
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)

