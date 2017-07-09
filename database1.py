                                        
import pymysql.cursors


db =pymysql.connect('localhost','root','raspberry','Smart_City')

try:
	with db.cursor() as cursor:
		trigger = 'hosp_push_1'


        	trig_1='1'
        	sql= ("INSERT INTO 'Apartment' ('Sensor_id', 'Sensor_name', 'Sensor_status') VALUES('%s', '%s', '%s'", ('ldr_id', 'LDR', 'Working'))
		cursor.execute(*sql)

finally:
#cursor.execute(*trig_b)
#cursor.execute(*trig_c)

	db.commit()
	db.close()



