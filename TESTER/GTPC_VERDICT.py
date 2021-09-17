def IECompare(IE, IR):
	for EveryElement in IE:
		if EveryElement in IR:
			if IE[EveryElement] == IR[EveryElement]:
				continue
			else:
				return "Test Case Failed with IE Field Value wrong :{}".format(EveryElement)
		else:
			return "Test Case failed with IE Field Missing {}".format(EveryElement)
	return "EQUAL"

def TestVerdict(DWAE, DWAR): #2
	for EveryKey in DWAE:
		if EveryKey in DWAR:
			if EveryKey == 'IEs':
				IECompareResult = IECompare(DWAE[EveryKey], DWAR[EveryKey])
				if IECompareResult == "EQUAL":
					continue
				else:
					return IECompareResult
				for EveryIE in DWAE[EveryKey]:
					if EveryIE in DWAR[EveryKey]:
						if EveryIE=='RECOVERY':
							IECompareResult = IECompare(DWAE[EveryKey][EveryIE], DWAR[EveryKey][EveryIE])
							if IECompareResult == "EQUAL":
								continue
							else:
								return IECompareResult
					else:
						return "Test case Failed With IE {} missing".format(EveryIE)
			else:
				if EveryKey !='MessageType':
					if DWAE[EveryKey] == DWAR[EveryKey]:
						continue
					else:
						if EveryKey == 'MessageLength':
							print "continuing by ignoring MessageLength Field mismatch"
							continue
						else:
							return "Test Case Failed with Header Field {} value Ex:{}, Value Rx:{}".format(EveryKey, DWAE[EveryKey],DWAR[EveryKey])
		else:
			return "Test Case Failed With Missing Field {}".format(EveryKey)
	return "Test Case Passed"
