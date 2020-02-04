#!/usr/bin/env python

import time
from networktables import NetworkTables

import logging	# Required
logging.basicConfig(level=logging.DEBUG)

NetworkTables.initialize()
table = NetworkTables.getTable("ML")
#print(str(table) + "this is a table")
#objects = table("nb_objects")
i = 0
while 1:
    #print("talking about " + str(objects) + "balls")


    time.sleep(1)

    if i == 100:
        i = 1