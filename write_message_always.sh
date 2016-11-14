#!/bin/bash

message="${@}"
path="/home/pi/madmug"
script="scroll-text-forever.py"

echo "\"${message}\"" | xargs python "${path}/${script}" &
