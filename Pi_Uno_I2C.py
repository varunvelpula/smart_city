import struct
import smbus
import time
import subprocess
#class Pi_Uno_I2C:  
bus = smbus.SMBus(1)
    
##    def uno_addresses(add1,add2,add3,add4):
##        self.add1=add1
##        self.add2=add2
##        self.add3=add3
##        self.add4=add4
        
    
def StringToBytes(val):
        retVal = []
        for c in val:
            retVal.append(ord(c))
        return retVal

def write_info(address,data_to_send_to_Arduino):
        try:
            bus.write_i2c_block_data(address,9,StringToBytes(data_to_send_to_Arduino))
        except IOError or  UnicodeDecodeError:
            print("IO_Error:I2C slave not detected")

def read_info(address):
        smsMessage = ""
	error_msg = "11111"
        try:
#	    print address	
#	    print bus
#           subprocess.call(['i2cdetect', '-y', '1'])
	    time.sleep(0.5)
	    data_received_from_Arduino = bus.read_i2c_block_data(address,9,17)
            #print(data_received_from_Arduino)
            # print("---")
#            for i in range(len(data_received_from_Arduino)):
#                smsMessage += chr(data_received_from_Arduino[i])
    
            #print(smsMessage.encode('utf-8'))
            print(smsMessage)	    	
       	    return(smsMessage);	
        except IOError or UnicodeDecodeError:
	    print("SLAVE NOT DETECTED")
#	    write_info(0x06, error_msg)	    
	    subprocess.call(['i2cdetect', '-y', '1'])



while True:
    
    print("-----------------------------------READING ALL---------------------------")
#    reply = read_info(0x06)	
#    print(reply)   
#    time.sleep(0.05)
#    reply = read_info(0x05)
#    print(reply)
#    time.sleep(0.05)
#    reply = read_info(0x04)
#    print(reply)
    time.sleep(0.05)
#    subprocess.call(['i2cdetect','-y','1'])	 
    reply = read_info(0x06)	
    print("------------------------------------DONE----------------------------------")
