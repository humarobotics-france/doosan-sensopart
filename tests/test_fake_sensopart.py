# -*- coding: utf-8 -*-
"""
Code made to simulate a SensoPart camera from a computer.
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

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

What does this example:
    1- Create 2 server (server_1 and server_2)
    2- Wait for a "TRG" from the DoosanSensoPart class
    3- return a static value (score;posx;posy;angle)
"""

import signal
import sys
import socket
import time

ADDRESS = "192.168.137.120"
PORT_1 = 2006
PORT_2 = 2005

print("Start first server")
server_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_1.bind((ADDRESS, PORT_1))
server_1.listen(1)
client_1, addressClient_1 = server_1.accept()
print('Server_1 connexion from ', addressClient_1)

print("Start second server")
server_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_2.bind((ADDRESS, PORT_2))
server_2.listen(1)
client_2, addressClient_2 = server_2.accept()
print('Server_2 connexion from ', addressClient_2)

def close_all_sockets():
    print('Close all clients connection')
    client_1.close()
    client_2.close()
    print('Stop servers')
    server_1.close()
    server_2.close()

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    close_all_sockets()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:

    while True:
        data = client_1.recv(1024)
        if not data:
            print('Error during recv')
        else:
            data = data.decode().upper()
            print('Recv of:' + data)
            if data == "TRG":
                response = "75;100;440;-180".encode() #'score; posx; posy; angle'
                res = client_2.send(response)
                if res != len(response):
                    print("Sending error")
                else:
                    print("Send ok")
        
        time.sleep(1)

finally: 
    close_all_sockets()