#from Pi_Uno_I2C import read_info
import time 
import smbus
bus=smbus.SMBus(1)
def StringToBytes(val):
        retVal = []
        for c in val:
            retVal.append(ord(c))
        return retVal

def write_info(address,data_to_send_to_Arduino):
        try:
            bus.write_i2c_block_data(address, 0x00,StringToBytes(data_to_send_to_Arduino))
        except IOError or  UnicodeDecodeError:
            print("IO_Error:I2C slave not detected")
def read_info(address):
        smsMessage = ""
        try:
            #print address
            #print bus
            data_received_from_Arduino = bus.read_i2c_block_data(address,5,17)
            print(data_received_from_Arduino)
            print("---")
            for i in range(len(data_received_from_Arduino)):
                smsMessage += chr(data_received_from_Arduino[i])

            #print(smsMessage.encode('utf-8'))
            print(smsMessage)
            return(smsMessage);
        except IOError or UnicodeDecodeError:
           print("SLAVE NOT DETECTED!")

'''while True:
	add=0x04
	sms_message=read_info(add)
	print(sms_message)
	time.sleep(0.05)'''
