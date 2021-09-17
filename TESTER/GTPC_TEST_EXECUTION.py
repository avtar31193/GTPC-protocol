#!/usr/bin/python

from GTPC_TEMPLATE import *
from GTPC_CODER import *
from GTPC_DECODER import *
from GTPC_TRANSPORT import *
from GTPC_VERDICT import *
import time
from socket import timeout as SUTReplyTimeout


ER_IN_BINARY = EchoRequestCoder(ECHO_REQUEST)
print ER_IN_BINARY

SUTPort = 2123
SUTIP = "10.0.3.15"
SUT = (SUTIP, SUTPort)
TesterSocket = GTPCTransport()
TesterSocket.sendto(ER_IN_BINARY,SUT)
TesterSocket.settimeout(30)

try:
	ERA_RX_FROM_SUT_HEX_BYTES = TesterSocket.recv(65535)
except SUTReplyTimeout:
	print "The Test Case Failed Due to SUT Reply Timeout"
else:
	ERA_RX_FROM_SUT_DECODED = GTPCDecoder(ERA_RX_FROM_SUT_HEX_BYTES)
	print ERA_RX_FROM_SUT_DECODED
	print TestVerdict(ECHO_RESPONSE, ERA_RX_FROM_SUT_DECODED)