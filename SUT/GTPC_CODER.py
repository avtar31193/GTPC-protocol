#!/usr/bin/python

import bitarray


def EchoRequestCoder(ERDict):
	ERBinary = bitarray.bitarray()
	ERBinary.extend(format(ERDict['Version'], '03b'))
	ERBinary.extend(format(ERDict['P'], '01b'))
	ERBinary.extend(format(ERDict['T'], '01b'))
	ERBinary.extend(format(ERDict['Spare1'], '01b'))
	ERBinary.extend(format(ERDict['Spare2'], '01b'))
	ERBinary.extend(format(ERDict['Spare3'], '01b'))
	ERBinary.extend(format(ERDict['MessageType'], '08b'))
	ERBinary.extend(format(ERDict['MessageLength'], '016b'))
	ERBinary.extend(format(ERDict['SequenceNumber'], '024b'))
	ERBinary.extend(format(ERDict['Spare4'], '08b'))
	ERBinary.extend(format(ERDict['IEs']['RECOVERY']['Type'], '08b'))
	ERBinary.extend(format(ERDict['IEs']['RECOVERY']['Length'], '016b'))
	ERBinary.extend(format(ERDict['IEs']['RECOVERY']['Spare'], '04b'))
	ERBinary.extend(format(ERDict['IEs']['RECOVERY']['Instance'], '04b'))
	ERBinary.extend(format(ERDict['IEs']['RECOVERY']['IE_SPECIFIC_DATA'], '08b'))



	return ERBinary

def EchoRequestCoder2(ERDict):
	ERBinary = bitarray.bitarray()
	ERBinary.extend(format(ERDict['Version'], '03b'))
	ERBinary.extend(format(ERDict['P'], '01b'))
	ERBinary.extend(format(ERDict['T'], '01b'))
	ERBinary.extend(format(ERDict['Spare1'], '01b'))
	ERBinary.extend(format(ERDict['Spare2'], '01b'))
	ERBinary.extend(format(ERDict['Spare3'], '01b'))
	ERBinary.extend(format(ERDict['MessageType'], '08b'))
	ERBinary.extend(format(ERDict['MessageLength'], '016b'))
	ERBinary.extend(format(ERDict['SequenceNumber'], '024b'))
	ERBinary.extend(format(ERDict['Spare4'], '08b'))



	return ERBinary