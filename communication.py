
import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

Broker = "192.168.42.1"

pub_topic_1 = "bot_sub/1"
sub_topic_1 = "bot_pub/1"

pub_topic_2 = "bot_sub/2"
sub_topic_2 = "bot_pub/2"

pub_topic_3 = "bot_sub/3"
sub_topic_3 = "bot_pub/3"

num = 0


def on_connect(client, userdata, flags, rc):
	if num == 1:
        	client.subscribe(sub_topic_1)
	elif num == 2:
		client.subscribe(sub_topic_2)
	elif num == 3:
		client.subscribe(sub_topic_3)

def on_message(client, userdata, msg):
        message = str(msg.payload)
        print(msg.topic+" "+message)
        
def publish_mqtt(sensor_data):
        mqttc = mqtt.Client("Client")
        mqttc.connect(Broker, 1883)
        
def on_publish(mosq, obj, mid):
        print("on_publish")
        
def bot_data(msg, pub_topic):
        client = mqtt.Client()
        #client.on_connect = on_connect
        #client.on_message = on_message 
        client.connect(Broker, 1883, 60)
        client.publish(pub_topic, msg) 
        #client.loop_forever()

def instruction(msg, n):
	global num
	num = n
	if num == 1:
		bot_data(msg, pub_topic_1)
	elif num == 2:
		bot_data(msg, pub_topic_2)
	elif num == 3:
		bot_data(msg, pub_topic_3)

bot_data('RLR', pub_topic_1)		 
#instruction('RFLFRS', 1)
print("SENT")
