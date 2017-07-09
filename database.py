import pymysql


db =pymysql.connect('localhost','root','raspberry','Smart_City')

cursor = db.cursor()
x='apt_push_1'
y='push1'
z='Working'	
sql= ("""INSERT INTO Apartment (Sensor_id, Sensor_name, Sensor_status) VALUES("%s", "%s", "%s")""", (x, y, z));

        
cursor.execute(*sql)

db.commit()
db.close()
