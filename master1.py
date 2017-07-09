from path_detection_1 import *
from path_planning_1 import *
from mqtt_pubsub import * 

b = path_planning_1(edge_destination,3) #edge number and vehicle number coming from serial communication
edge_no = path_detection_1()
#instruction(b) # path sent to the bots