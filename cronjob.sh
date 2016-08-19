#!/bin/bash

mpg123_installed=1
notify_send_installed=1
type mpg123 >/dev/null 2>&1 || mpg123_installed=0
type notify-send >/dev/null 2>&1 || notify_send_installed=0

if [[ mpg123_installed -eq 0 || notify_send_installed -eq 0 ]]; then
    if [[ mpg123_installed -eq 0 ]]; then
        echo "mpg123 isn't installed. Use sudo apt install mpg123";
    fi
    if [[ notify_send_installed -eq 0 ]]; then
        echo "notify-send isn't installed. Use sudo apt install notify-send";
    fi
    exit 1
fi

environ=/proc/$(pgrep gnome-session)/environ
eval "export $(egrep -z DBUS_SESSION_BUS_ADDRESS $environ)"
eval "export $(egrep -z DISPLAY $environ)"
eval "export $(egrep -z XDG_RUNTIME_DIR $environ)"

python main.py $@