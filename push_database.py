import pymysql

#db = pymysql.connect('localhost', 'root', 'raspberry', 'Smart_City')
#cursor = db.cursor()
add=0x04
msg = ""
flag = 0
trig_1=0
trig_2=0
trig_3=0

sen_1=0
sen_2=0
sen_3=0
sen_4=0
sen_5=0
sen_6=0
sen_7=0

def binary_data(mark, m):
	global trig_1, trig_2, trig_3, sen_1, sen_2, sen_3, sen_4, sen_5, msg
	msg = m
	trig_1 = msg[mark]
	trig_2 = msg[mark+1]
	trig_3 = msg[mark+2]
	sen_1 = msg[mark+3]
	sen_2 = msg[mark+4]
	sen_3 = msg[mark+5]
	sen_4 = msg[mark+6]
	sen_5 = msg[mark+7]

def integer_data(mark,m):
	global sen_6, sen_7, msg
	msg = m
	sen_6 = msg[mark:mark+2]
	if msg[mark+2] == '|':
		sen_7 = msg[mark+3:mark+5]

#def cmd(mark):

def print_data():
	global trig_1, trig_2, trig_3, sen_1, sen_2, sen_3, sen_4, sen_5, sen_6, sen_7
	print trig_1 
	print trig_2
	print trig_3
	print sen_1
	print sen_2
	print sen_3
	print sen_4
	print sen_5
	print sen_6
	print sen_7

def apart_push():
	global trig_1, trig_2, trig_3, sen_1, sen_2, sen_3, sen_4, sen_5, sen_6, sen_7
	
	db = pymysql.connect('localhost', 'root', 'raspberry', 'Smart_City')
	cursor = db.cursor()

	aprt_del = "TRUNCATE Apartment"
	cursor.execute(aprt_del)
	
	aprt_1 = ('INSERT INTO Apartment (Sensor_id, Sensor_name, Sensor_status) VALUES("apt_ir", "garbage status","%s")', (sen_1));
        aprt_2 = ('INSERT INTO Apartment (Sensor_id, Sensor_name, Sensor_status) VALUES("apt_ldr_top", "top status","%s")', (sen_2));
	aprt_3 = ('INSERT INTO Apartment (Sensor_id, Sensor_name, Sensor_status) VALUES("apt_ldr_wall", "wall status","%s")', (sen_3));
	aprt_4 = ('INSERT INTO Apartment (Sensor_id, Sensor_name, Sensor_status) VALUES("apt_lm35", "temperature","%s")', (sen_4));
	aprt_5 = ('INSERT INTO Apartment (Sensor_id, Sensor_name, Sensor_status) VALUES("apt_smoke", "smoke status","%s")', (sen_5));
	aprt_6 = ('INSERT INTO Apartment (Sensor_id, Sensor_name, Sensor_status) VALUES("apt_ldr_wall", "wall status","%s")', (sen_6));
        aprt_7 = ('INSERT INTO Apartment (Sensor_id, Sensor_name, Sensor_status) VALUES("apt_lm35", "temperature","%s")', (sen_7));

	aprt_8 = ('INSERT INTO Apartment (Sensor_id, Sensor_name, Sensor_status) VALUES("apt_push_1", "push 1","%s")', (trig_1));
	aprt_9 = ('INSERT INTO Apartment (Sensor_id, Sensor_name, Sensor_status) VALUES("apt_push_2", "push 2","%s")', (trig_2));
	aprt_10 = ('INSERT INTO Apartment (Sensor_id, Sensor_name, Sensor_status) VALUES("apt_push_3", "push 3","%s")', (trig_3));
		
	cursor.execute(*aprt_1)
	cursor.execute(*aprt_2)
	cursor.execute(*aprt_3)
	cursor.execute(*aprt_4)
	cursor.execute(*aprt_5)
	cursor.execute(*aprt_6)
	cursor.execute(*aprt_7)
	cursor.execute(*aprt_8)
	cursor.execute(*aprt_9)
        cursor.execute(*aprt_10)

	db.commit()
        db.close()



def hosp_push():
	
	global trig_1, trig_2, trig_3, sen_1, sen_2, sen_3, sen_4, sen_5, sen_6, sen_7

	db = pymysql.connect('localhost', 'root', 'raspberry', 'Smart_City')
	cursor = db.cursor()

	hosp_del = "TRUNCATE Hospital"
	cursor.execute(hosp_del)

	aprt_1 = ('INSERT INTO Hospital (Sensor_id, Sensor_name, Sensor_status) VALUES("hosp_lcd", "lcd display","%s")', (sen_1));
	aprt_2 = ('INSERT INTO Hospital (Sensor_id, Sensor_name, Sensor_status) VALUES("hosp_smoke", "smoke status","%s")', (sen_2));
	aprt_3 = ('INSERT INTO Hospital (Sensor_id, Sensor_name, Sensor_status) VALUES("hosp_ir_garbage", "garbage status","%s")', (sen_3));
	aprt_4 = ('INSERT INTO Hospital (Sensor_id, Sensor_name, Sensor_status) VALUES("hosp_ir_gate", "gate status","%s")', (sen_4));
	aprt_5 = ('INSERT INTO Hospital (Sensor_id, Sensor_name, Sensor_status) VALUES("hosp_ldr", "conveyer","%s")', (sen_5));
	aprt_6 = ('INSERT INTO Hospital (Sensor_id, Sensor_name, Sensor_status) VALUES("hosp_lm35", "temperature","%s")', (sen_6));
	#aprt_7 = ('INSERT INTO Hospital (Sensor_id, Sensor_name, Sensor_status) VALUES("apt_lm35", "temperature","%s")', (sen_7));

	aprt_8 = ('INSERT INTO Hospital (Sensor_id, Sensor_name, Sensor_status) VALUES("hosp_push_1", "push 1","%s")', (trig_1));
	aprt_9 = ('INSERT INTO Hospital (Sensor_id, Sensor_name, Sensor_status) VALUES("hosp_push_2", "push 2","%s")', (trig_2));
	aprt_10 = ('INSERT INTO Hospital (Sensor_id, Sensor_name, Sensor_status) VALUES("hosp_push_3", "push 3","%s")', (trig_3));

	cursor.execute(*aprt_1)
	cursor.execute(*aprt_2)
	cursor.execute(*aprt_3)
	cursor.execute(*aprt_4)
	cursor.execute(*aprt_5)
	cursor.execute(*aprt_6)
	#cursor.execute(*aprt_7)
	cursor.execute(*aprt_8)
	cursor.execute(*aprt_9)
	cursor.execute(*aprt_10)

	db.commit()
	db.close()


#def mall_push():

def school_push():
	global trig_1, trig_2, trig_3, sen_1, sen_2, sen_3, sen_4, sen_5, sen_6, sen_7

        db = pymysql.connect('localhost', 'root', 'raspberry', 'Smart_City')
        cursor = db.cursor()

        school_del = "TRUNCATE School"
        cursor.execute(school_del)

        school_1 = ('INSERT INTO School (Sensor_id, Sensor_name, Sensor_status) VALUES("school_smoke", "smoke status","%s")', (sen_1));
        school_2 = ('INSERT INTO School (Sensor_id, Sensor_name, Sensor_status) VALUES("school_ir_garbage", "garbage status","%s")', (sen_2));
        school_3 = ('INSERT INTO School (Sensor_id, Sensor_name, Sensor_status) VALUES("school_ir_room_1", "room 1 status","%s")', (sen_3));
        school_4 = ('INSERT INTO School (Sensor_id, Sensor_name, Sensor_status) VALUES("school_ir_room_2", "room 2 status","%s")', (sen_4));
        school_5 = ('INSERT INTO School (Sensor_id, Sensor_name, Sensor_status) VALUES("school_lm35", "temperature","%s")', (sen_5));
        school_6 = ('INSERT INTO School (Sensor_id, Sensor_name, Sensor_status) VALUES("school_ldr", "lighting status","%s")', (sen_6));
        #aprt_7 = ('INSERT INTO Hospital (Sensor_id, Sensor_name, Sensor_status) VALUES("apt_lm35", "temperature","%s")', (sen_7));

        school_8 = ('INSERT INTO School (Sensor_id, Sensor_name, Sensor_status) VALUES("school_push_1", "push 1","%s")', (trig_1));
        school_9 = ('INSERT INTO School (Sensor_id, Sensor_name, Sensor_status) VALUES("school_push_2", "push 2","%s")', (trig_2));
        school_10 = ('INSERT INTO School (Sensor_id, Sensor_name, Sensor_status) VALUES("school_push_3", "push 3","%s")', (trig_3));

        cursor.execute(*school_1)
        cursor.execute(*school_2)
        cursor.execute(*school_3)
        cursor.execute(*school_4)
        cursor.execute(*school_5)
        cursor.execute(*school_6)
        #cursor.execute(*aprt_7)
        cursor.execute(*school_8)
        cursor.execute(*school_9)
        cursor.execute(*school_10)

        db.commit()
        db.close()


#flag = flag+2
#msg=read_info(add)
#print("MESSAGE"+msg)
#if msg[flag] == '0' and msg[flag+1] == '4':
#	flag = flag+3
#	binary_data(flag)
#	flag = flag+9
#	integer_data(flag)
#	print_data()
#	apart_push()	
#	db.commit()
#	db.close()

