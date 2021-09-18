#!/usr/bin/python 

ECHO_REQUEST = {
	'Version':2,
	'P':0,
	'T':0,
	'Spare1':0,
	'Spare2':0,
	'Spare3':0,	
	'MessageType':1,
	'MessageLength':3+1,
	'SequenceNumber':0,
	'Spare4':0,
	'IEs':{
		'RECOVERY':{
				'Type':3,
				'Length':1,
				'Spare':0,
				'Instance':0,
				'IE_SPECIFIC_DATA':0
		}
	}	
}

ECHO_RESPONSE = {
	'Version':2,
	'P':0,
	'T':0,
	'Spare1':0,
	'Spare2':0,
	'Spare3':0,	
	'MessageType':2,
	'MessageLength':3+1,
	'SequenceNumber':0,
	'Spare4':0,
	'IEs':{
		'RECOVERY':{
				'Type':3,
				'Length':1,
				'Spare':0,
				'Instance':0,
				'IE_SPECIFIC_DATA':0
		}
	}	
}

