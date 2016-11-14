#!/bin/bash

ps aux | grep "madmug" | grep -v grep | tr -s " " | cut -d" " -f2 | xargs kill

