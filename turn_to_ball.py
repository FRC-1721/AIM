#initialize and imports, do not edit
import sys
import time
import frc.robot
from networktables import NetworkTables

import logging
logging.basicConfig(level=logging.DEBUG)

if len(sys.argv) != 2:
    print("Error: specify an IP to connect to!")
    exit(0)

ip = sys.argv[1]

NetworkTables.initialize(server=ip)
table = NetworkTables.getTable("ML")

#values for tweaking

#math & code
while 1:
    b1cX.getNumber('ball1centerX', 0)
    b2cX.getNumber('ball2centerX', 0)

