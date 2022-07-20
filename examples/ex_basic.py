# -*- coding: utf-8 -*-
"""
A basic example to communicate between a SensoPart, using DoosanSensoPart, class and the Doosan.
Please read the README.md file before use.

Copyright (C) 2022 HumaRobotics

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

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
