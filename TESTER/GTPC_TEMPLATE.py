#!/usr/bin/python 

ECHO_REQUEST = {
	'Spare1':0,
	'Spare2':0,
	'Spare3':0,
	'T':0,
	'P':0,
	'Version':2,
	'MessgaeType':1,
	'MessageLength':13,
	'SequenceNumber':0,
	'Spare4':0
	'IEs':{
		'RECOVERY':{
				'Type':3,
				'Length':5,
				'Spare':0,
				'Instance':0,
				'Recovery':0,
			},
			'PRIVATE_EXTENSION':0
	}	
}

ECHO_RESPONSE = {
	'Spare1':0,
	'Spare2':0,
	'Spare3':0,
	'T':0,
	'P':0,
	'Version':2,
	'MessgaeType':2,
	'MessageLength':13,
	'SequenceNumber':0,
	'Spare4':0
	'IEs':{
		'RECOVERY':{
				'Type':3,
				'Length':5,
				'Spare':0,
				'Instance':0,
				'Recovery':0,
		},
		'CAUSE'=0
		'PRIVATE_EXTENSION'=0
	}	
}