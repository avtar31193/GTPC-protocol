#!/usr/bin/python

import socket
import sctp
from GTPC_CODER import *
from GTPC_TEMPLATE import *
import time

SUTPort = 2123
SUTIP = "10.0.3.15"
SUT = (SUTIP, SUTPort)

SUTSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
SUTSocket.bind(SUT)

MessageFromTester,FromWhomMessageArrived = SUTSocket.recvfrom(65535)
print MessageFromTester

ER_Binary_Perfect = EchoRequestCoder(ECHO_RESPONSE_PERFECT)
ER_Binary_WRONG_IE_Data = EchoRequestCoder(ECHO_RESPONSE_Wrong_IE)
ER_Binary_IE_Missing = EchoRequestCoder2(ECHO_RESPONSE_MISSING_IE)

SUTChoice = input("Choose an option from the following behaviors of SUT:\n\
					1. For Perfect Response \n\
					2. For Wrong IE Data \n\
					3. For Missing IE \n\
					4. Timeout with No Reply \n\
					Your input options among(1,2,3,4) is:")

if SUTChoice == 1:
	SUTSocket.sendto(ER_Binary_Perfect,FromWhomMessageArrived)
elif SUTChoice == 2:
	SUTSocket.sendto(ER_Binary_WRONG_IE_Data,FromWhomMessageArrived)
elif SUTChoice == 3:
	SUTSocket.sendto(ER_Binary_IE_Missing,FromWhomMessageArrived)
elif SUTChoice == 4:
	time.sleep(45)


SUTSocket.close()