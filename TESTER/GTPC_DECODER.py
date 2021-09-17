#!/usr/bin/python

import bitarray

def GTPCDecoder(HB):
	ERA_Dict = dict()
	MSG_RX_IN_BINARY = bitarray.bitarray()
	MSG_RX_IN_BINARY.frombytes(HB)
	ERA_Dict.update({'Version':int(MSG_RX_IN_BINARY[0:3].to01(), 2)})
	ERA_Dict.update({'P':int(MSG_RX_IN_BINARY[3:4].to01(), 2)})
	ERA_Dict.update({'T':int(MSG_RX_IN_BINARY[4:5].to01(), 2)})
	ERA_Dict.update({'Spare1':int(MSG_RX_IN_BINARY[5:6].to01(), 2)})
	ERA_Dict.update({'Spare2':int(MSG_RX_IN_BINARY[6:7].to01(), 2)})
	ERA_Dict.update({'Spare3':int(MSG_RX_IN_BINARY[7:8].to01(), 2)})
	
	

	ERA_Dict.update({'MessageType':int(MSG_RX_IN_BINARY[8:16].to01(), 2)})
	ERA_Dict.update({'MessageLength':int(MSG_RX_IN_BINARY[16:32].to01(), 2)})
	ERA_Dict.update({'SequenceNumber':int(MSG_RX_IN_BINARY[32:56].to01(), 2)})
	ERA_Dict.update({'Spare4':int(MSG_RX_IN_BINARY[56:64].to01(), 2)})
	if ERA_Dict['MessageLength']==4:
		ERA_Dict.update({'IEs':{'RECOVERY':{'Type':int(MSG_RX_IN_BINARY[64:72].to01(), 2),'Length':int(MSG_RX_IN_BINARY[72:88].to01(), 2),'Spare':int(MSG_RX_IN_BINARY[88:92].to01(), 2),'Instance':int(MSG_RX_IN_BINARY[92:96].to01(), 2),'IE_SPECIFIC_DATA':int(MSG_RX_IN_BINARY[96:104].to01(), 2)}}})
		return ERA_Dict
	else:
		return ERA_Dict
	

