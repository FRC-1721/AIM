#initialize and imports, do not edit
import sys
import time

from networktables import NetworkTables

import logging
logging.basicConfig(level=logging.DEBUG)

NetworkTables.initialize(server="10.17.21.2")
table = NetworkTables.getTable("ML")
NetworkTables.setServer([("10.17.21.2", 5800), ])

#values for tweaking
turnSpeed = 0.2
#math & code
while 1:
    b1cX.getNumber('ball1centerX', 0)
    b2cX.getNumber('ball2centerX', 0)

    leftSpeed = 0
    rightSpeed = 0
    if (ball1centerX >=25 and ball1centerX <= 35):
        pass
    elif(ball1centerX < 25):
        leftSpeed = turnSpeed
    elif(ball1centerX > 35):
        rightSpeed = turnSpeed
    
        
    
    ros.putNumber("coprocessorPort", leftSpeed)
    ros.putNumber("coprocessorStarboard", rightSpeed)

