#!/usr/bin/python

import socket
import sctp

def GTPCTransport():
	TesterPort = 2123
	TesterIP = "10.0.2.15"
	Tester = (TesterIP, TesterPort)

	SUTPort = 2123
	SUTIP = "10.0.3.15"
	SUT = (SUTIP, SUTPort)

	TesterSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #IPV4
	TesterSocket.bind(Tester)


	return TesterSocket