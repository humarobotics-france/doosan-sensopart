# -*- coding: utf-8 -*-
"""
An example to perform hand eye calibration with a SensoPart camera.
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
    - Add calibration points Global_p1, Global_p2, ..., Global_p9
    - change 'ip' variable if necessary
    - change portIN and portOUT if necessary

What does this example:
    1- Connection to the camera
    2- Init calibration
    3- Move the robot and add a calibration image x 9
    4- Run calibration
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

sensopart.calibration_init()

movej(Global_p1) # First calibration point
sensopart.add_calibration_image(measurement_plane="1") # Only for the first image

movej(Global_p2)
sensopart.add_calibration_image()

movej(Global_p3)
sensopart.add_calibration_image()

movej(Global_p4)
sensopart.add_calibration_image()

movej(Global_p5)
sensopart.add_calibration_image()

movej(Global_p6)
sensopart.add_calibration_image()

movej(Global_p7)
sensopart.add_calibration_image()

movej(Global_p8)
sensopart.add_calibration_image()

movej(Global_p9)
sensopart.add_calibration_image()

sensopart.run_calibration()