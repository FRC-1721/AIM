#initialize and imports, do not edit
import sys
import time

from networktables import NetworkTables
import logging
logging.basicConfig(level=logging.DEBUG)

rosserver = NetworkTables
rosserver.initialize(server="10.17.21.2")
NetworkTables.setServer([("10.17.21.2", 5800), ])

mlserver = NetworkTables
mlserver.initialize(server="10.17.21.2")

mltable = mlserver.getTable("ML")
rostable = rosserver.getTable("ROS")



#values for tweaking
turnSpeed = 0.5
#math & code
while 1:
    b1cx = mltable.getNumber('ball1centerX', 0)

    leftSpeed = 0
    rightSpeed = 0
    if (b1cx >=25 and b1cx <= 35):
        leftSpeed = 0
        rightSpeed = 0
    elif(b1cx < 25 and b1cx != 0):
        leftSpeed = turnSpeed
    elif(b1cx > 35):
        rightSpeed = turnSpeed
    else:
        leftSpeed = 0
        rightSpeed = 0
  
        

    rostable.putNumber("coprocessorPort", 1)
    rostable.putNumber("coprocessorStarboard", 1)
    
    test = rostable.getNumber("coprocessorPort", 45)
    
    print(rightSpeed)
    print(leftSpeed)
    print(test)


