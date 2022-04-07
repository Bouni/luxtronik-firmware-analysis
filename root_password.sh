#!/bin/sh

if ! command -v john &> /dev/null;
then
    echo "john seems not to be installed, install it to use this script"
    echo "More infos: https://www.openwall.com/john/"
    exit
fi



# Unshadow if shadow and passwd files are part of the firmware
if test -f "firmware/share/passwd" && test -f "firmware/share/shadow"; then
    echo "passwd and shadow exists, attempt to get root password."
    unshadow "firmware/share/passwd" "firmware/share/shadow" > unshadow.txt
    cracked=$(john --show unshadow.txt 2> /dev/null | grep root)
    user=$(echo $cracked | cut -d ':' -f 1)
    password=$(echo $cracked | cut -d ':' -f 2)
    rm unshadow.txt
    echo "Username: $user"
    echo "Password: $password"
else
    echo "No firmware/share/passwd or firmware/share/shadow file found"
fi
