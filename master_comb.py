#from communication import * 
#from push_database import *
from path_planning_new import *
#from Pi_comms_test import read_info
from path_detection_1 import *

flag=0
edge_no_1 = [1,2]

bot_no = 1
graph =[]

source_1=0
source_2=0
source_3=0
previous_1=0
previous_2=0
previous_3=0


def adj_matrix():
	global graph, previous_1, previous_2, previous_3, source_1, source_2, source_3
	
	bots = imageprocessing()
	
	graph = [[0,3,0,3,1,0,0,0],
            [3,0,3,0,0,1,0,0],
            [0,3,0,3,0,0,1,0],
            [3,0,3,0,0,0,0,1],
            [1,0,0,0,0,1,0,1],
            [0,1,0,0,1,0,1,0],
            [0,0,1,0,0,1,0,1],
            [0,0,0,1,1,0,1,0]]
	stored_graph=copy.deepcopy(graph)
	previous_1 = bots[0][0]
	previous_2 = bots[1][0]
	previous_3 = bots[2][0]

	source_1 = bots[0][1]
	source_2 = bots[1][1]
	source_3 = bots[2][1]

def bot1_call(edge_no):
	global source_1, previous_1, graph
	b, source_1, previous_1, graph = path_planning(edge_no, 1, source_1, previous_1, graph)
	return b

def bot2_call(edge_no):
        global  source_2, previous_2, graph                               
        b, source_2, previous_2, graph = path_planning(edge_no, 2, source_2, previous_2, graph)
        return b

def bot3_call(edge_no):
        global source_3, previous_3, graph                               
        b, source_3, previous_3, graph = path_planning(edge_no, 3, source_3, previous_3, graph)
        return b

def logging(add):
	ap = 0
	ap = ap+2
	msg=read_info(add)
	print msg
	if msg[ap] == '0' and msg[ap+1] == '8':
	       	ap = ap+3
		binary_data(ap, msg)
		ap = ap+9
		integer_data(ap, msg)
		#print_data()
		hosp_push()    
	elif msg[ap] == '0' and msg[ap+1] == '6':
                ap = ap+3
                binary_data(ap, msg)
                ap = ap+9
                integer_data(ap, msg)
                print_data()
                apart_push()
	elif msg[ap] == '0' and msg[ap+1] == '5':
                ap = ap+3
                binary_data(ap, msg)
                ap = ap+9
                integer_data(ap, msg)
                #print_data()
                school_push()
	elif msg[ap] == '0' and msg[ap+1] == '7':
                ap = ap+3
                binary_data(ap, msg)
                ap = ap+9
                integer_data(ap, msg)
                #print_data()
                mall_push()


#path planning

#if flag<1:
adj_matrix()
b = bot2_call(edge_no_1)
print b
clear_path(1, graph)

#i2c

#logging(0x06)

#botcomm

#instruction(b)

#image processing



