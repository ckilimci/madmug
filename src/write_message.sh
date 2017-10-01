#!/bin/bash

message="${@}"
path="/home/pi/madmug"
script="scroll-text-once.py"

echo "\"${message}\"" | xargs python "${path}/${script}" 
