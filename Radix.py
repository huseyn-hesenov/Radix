strEded = str(input("Zehmet olmasa 3 reqemli ededi daxil edin:"))
tempEded = strEded
if (len(strEded) != 3) or not strEded.isdigit():
    print("Daxil etdiyini melumat sehvdir")
else:
    intEded = int(strEded)
    maxReqem = max(int(strEded[0]), int(strEded[1]),
int(strEded[2]))
    minReqem = min(int(strEded[0]), int(strEded[1]),
int(strEded[2]))
    if int(tempEded[0]) == maxReqem:
        tempEded = tempEded[1:]
    elif int(tempEded[1]) == maxReqem:
        tempEded = tempEded[0] + tempEded[2]
    else:
        tempEded = tempEded[:2]
    if int(tempEded[0]) == minReqem:
        tempEded = tempEded[1]
    else:
        tempEded = tempEded[0]
        newNumber = int(str(maxReqem) + str(tempEded) +
        str(minReqem))
    if newNumber == intEded:
        print("The Biggest Number")
    else:
        print(newNumber)