import smbus
import time
import struct
bus=smbus.SMBus(1)

def StringToBytes(val):
        retVal = []
        for c in val:
            retVal.append(ord(c))
        return retVal


def write_info(add,data):
	try:
		bus.write_i2c_block_data(add,9,data)
		print("WROTE DATA")
	except IOError or UnicodeDecodeError,(ErrorNumber,ErrorMessage):
	     print("WRITE IO_ERROR"+" "+str(ErrorNumber)+" "+str(ErrorMessage))
	
def read_info(add):
	smsMessage= ""
	try:
		data=bus.read_i2c_block_data(add,55,17)
		print("=====")
#		print(data)
		for i in range(len(data)):
	            if(data[i]!=255):  
 			  smsMessage += chr(data[i])
		print(smsMessage)
		print("====")
		return smsMessage
	except IOError or UnicodeDecodeError,(ErrorNumber,ErrorMessage):
	     print("READ IO_ERROR"+" "+str(ErrorNumber)+" "+str(ErrorMessage))
	     return "None"


#while True:
#	read_info(0x05)
#	time.sleep(0.1)
	
#	read_info(0x06)
#	time.sleep(0.1)
	
#	read_info(0x07)
#	time.sleep(0.1)
	
#	read_info(0x08)
#	time.sleep(0.1)	
