# -*- coding: utf-8 -*-
"""
A basic example to communicate between a SensoPart, using DoosanSensoPart, class and the Doosan.
Please read the README.md file before use.
Copyright (C) 2021 HumaRobotics

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

In your Task Writer/ Task Builder you need:
    - A 'CustomCode' with the 'DoosanSensoPart' file
    - A 'CustomCode' with this file
    - change 'ip' variable if necessary
    - change portIN and portOUT if necessary
    - adapt posz, angle_rx, angle_ry values to your robot configuration 

What does this example:
    1- Connection to the camera
    2- Send a "TRG" to the camera
    3- Read return values from the camera
    4- Extract data
    5- Move to posx, posy, posz, angle_rx, angle_ry, angle_rz if score > 50
"""

# Keep thoses lines in order to test the code without a Doosan:
import sys
import os
import time
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from DoosanSensoPart import DoosanSensoPart
wait = time.sleep

def movejx(pos, sol):
    movejx = print("pos:", pos, "sol:", sol)
# Remove lines above when you want to used this code on the robot

camera_ip = "192.168.137.120"
sensopart = DoosanSensoPart(ip=camera_ip, portIN=2006, portOUT=2005)

sensopart.TRG()  # Send a triger to the camera
wait(0.2)
res, rx_data = sensopart.read()  # read value returning by the camera
(score, pos_x, pos_y, angle_rz) = sensopart.extract_data(rx_data)

posz = 40
angle_rx = 0
angle_ry = 180
if score > 50:
    movejx([pos_x, pos_y, posz, angle_rx, angle_ry, angle_rz], sol=2)
