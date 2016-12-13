#!/bin/bash

ps aux | grep "madmug" | grep -v grep | grep -v madmugbot | grep -v buttoncontrol | tr -s " " | cut -d" " -f2 | xargs kill

