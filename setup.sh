#!/bin/bash

echo "Enabling Camera"
#yes, 0=on, 1=off
sudo raspi-config nonint do_camera 0

echo "Updating System"
sudo apt update
yes | sudo apt dist-upgrade

echo "Installing prerequirements"
yes | sudo apt install openbox xorg python3 python3-picamera python3-pyqt5 python3-pyqt5.qtwebkit lightdm python3-rpi.gpio git
# Suggested tools: sxiv tmux vim usbmount x11vnc

echo "Installing Fotobox"
git clone https://github.com/adlerweb/fotobox.git /home/pi/fotobox

echo "Configuring autostart"
mkdir -p ~/.config/openbox
echo "xset s noblank" >> ~/.config/openbox/autostart
echo "xset s off" >> ~/.config/openbox/autostart
echo "xset -dpms" >> ~/.config/openbox/autostart
echo "cd ~/fotobox/ ; python3 fotobox.py | tee fotobox.log" >> ~/.config/openbox/autostart
# GUI-Boot with autologin
sudo raspi-config nonint do_boot_behaviour B4

echo "Syncing..."
sudo sync

