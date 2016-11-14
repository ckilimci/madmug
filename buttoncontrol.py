#!/usr/bin/python

from gpiozero import Button
from signal import pause
import netifaces
import subprocess

path = "/home/pi/madmug/"

def say_green():
    say_orange()
    print("Screen will show time")
    cmd = path + "time.sh"
    subprocess.Popen([cmd])
    print("Done!")

def say_yellow():
    say_orange()
    cmd = path + "write_message.sh"
    ip = netifaces.ifaddresses("wlan0")[netifaces.AF_INET][0]["addr"]
    cmd_list = []
    cmd_list.append(cmd)
    cmd_list.append(ip)
    subprocess.Popen(cmd_list)
    print('IP: [' + ip +'] is shown.')

def say_orange():
    print("Every scrollphat process will stop")
    cmd = path + "stop_all.sh"
    subprocess.Popen([cmd])
    print("Stoped!")
    cmd = path + "clear_screen.sh"
    subprocess.Popen([cmd])
    print("Cleared!")

def say_red():
    say_orange()
    print("Screen will show some message")
    cmd = path + "write_message_always.sh"
    subprocess.Popen([cmd, "Selam :)"])
    print("Done!")


green = 16
yellow = 19
orange = 26
red = 20
button1 = Button(green)
button2 = Button(yellow)
button3 = Button(orange)
button4 = Button(red)

button1.when_pressed = say_green
button2.when_pressed = say_yellow
button3.when_pressed = say_orange
button4.when_pressed = say_red

pause()