b=bytes([68,69,70])
print("Bytes:",b)
ba=bytearray([65,66,67])
print("Bytearray before:",ba)
ba[0]=97
print("Bytearray update:",ba)
ba.append(68)
print("After the append:",ba)