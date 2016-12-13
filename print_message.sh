#!/bin/bash

sender="${1}"
message="${@:2}"
echo "sender:${sender}"
echo "message:${message}"
path="/home/pi/madmug"
script="myprinter.py"

echo "\"${sender}\" \"${message}\"" | xargs sudo python "${path}/${script}" 
