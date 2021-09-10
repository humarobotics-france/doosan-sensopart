# -*- coding: utf-8 -*-
"""
An example to perform hand eye calibration with a SensoPart camera.
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