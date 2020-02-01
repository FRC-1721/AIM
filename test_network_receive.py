#!/usr/bin/env python
# from robotpy.readthedocs.io


import sys
import time
from networktables import NetworkTables

import logging	# Required
logging.basicConfig(level=logging.DEBUG)

if len(sys.argv) != 2:
    print("Error: specify an IP to connect to!")
    exit(0)

ip = sys.argv[1]

smoothLevel = 10

NetworkTables.initialize(server=ip)
table = NetworkTables.getTable("ML")
i = 0
ball1memX = 0
while 1:
    object1posX = table.getNumberArray('boxes', [0,0,0,0])
    numBall = table.getNumber('nb_objects', 0)
    try:    
        ball1centerX = ((object1posX[2]-object1posX[0])/2 + object1posX[0])/5.33
    except:
        pass
    if (numBall == 1):
        try:     
            ball1memX = ball1centerX 
            i = 0
        except:
            pass

    if (i >= smoothLevel):
        ball1memX = 0
    else:
        pass

    if (numBall == 1):
        try:     
            print("The center of ball 1 is at " + str(ball1memX))
        except:
            print("not enough ballage")
    elif (numBall == 2):
        print("The center of ball 1 is at " + str(((object1posX[2]-object1posX[0])/2 + object1posX[0]/5.33)))
        print("The center of ball 2 is at " + str(((object1posX[3]-object1posX[1])/2 + object1posX[1]/5.33)))
    elif (numBall > 2):
        print("Too many balls")
    elif (numBall <= 0):
        if (i <= 19):
            print("The center of ball 1 is at " + str(ball1memX))
        else:
           print("not enough ballage")
    i = i + 1
    time.sleep(0.2)
