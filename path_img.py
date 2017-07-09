# The implememted image processing and path planning code
import math
import numpy as np
import cv2
import cv2.aruco as aruco

def path_planning(destination, previous, vehicle_no):

    def check_turn(i):

            (x0,y0) = path_array[i]
            (x1,y1) = path_array[i+1]
            (x2,y2) = path_array[i+2]

            d  =((x2 - x1)*(y0 - y1) -(y2 - y1)*(x0 - x1))

            if d>0:
                    return 'L'
            if d<0:
                    return 'R'

    def get_angle(i):
            (x0,y0) = path_array[i+0]
            (x1,y1) = path_array[i+1]
            (x2,y2) = path_array[i+2]

            dx1 = x1-x0
            dy1 = y1-y0
            dx2 = x2-x1
            dy2 = y2-y1

            d = dx1*dx2 + dy1*dy2
            l2 = (dx1*dx1+dy1*dy1)*(dx2*dx2+dy2*dy2)

            angle = math.acos(d/math.sqrt(l2))

            ans = (angle*(180/math.pi))
            return ans

    def turn_complement(turn):
            if turn== 'R':
                    complement ='L'
            else:
                    complement ='R'
            return complement

    def final_answer(path_array):
            array = []
            
            for i in range(0,(len(path_array)-2)):
                    (x0,y0) = path_array[i+0]
                    (x1,y1) = path_array[i+1]
                    (x2,y2) = path_array[i+2]
                    
                    turn = check_turn(i)
                    angle = get_angle(i)
                    if (x1,y1) == n0 or (x1,y1) == n1 or (x1,y1)==n2 or (x1,y1)==n3:
                        if angle<50:
                                turn = turn_complement(turn)
                    array.append(turn)
	    #print array
	    message = ''.join(array)
            message = message+'S'
            print message
	    return message

    rr=[]


# In[71]:

    from collections import defaultdict
 
#Class to represent a graph
    class Graph:
        # A utility function to find the vertex with minimum dist value, from
        # the set of vertices still in queue
        def minDistance(self,dist,queue):
            # Initialize min value and min_index as -1
            minimum = float("Inf")
            min_index = -1
            #from the dist array,pick one which has min value and is till in queue``1
            for i in range(len(dist)):
                if dist[i] < minimum and i in queue:
                    minimum = dist[i]
                    min_index = i
            return min_index


        # Function to print shortest path from source to j
        # using parent array
        def printPath(self, parent, j):
            if parent[j] == -1 : #Base Case : If j is source
                #print j,
                rr.append(j)
                return
            self.printPath(parent , parent[j])
            #print j,
            rr.append(j)


        # A utility function to print the constructed distance
        # array
        def printSolution(self, dist, parent,dest):
            #src = 0
            #print("Vertex \t\tDistance from Source\tPath") 
            #for i in range(1, len(dist)):
            #    print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i])),
            #    self.printPath(parent,i)
            i=dest
            self.printPath(parent,i)


        '''Function that implements Dijkstra's single source shortest path
        algorithm for a graph represented using adjacency matrix
        representation'''
        def dijkstra(self, graph, src, dest):
            row = len(graph)
            col = len(graph[0])

            # The output array. dist[i] will hold the shortest distance from src to i
            # Initialize all distances as INFINITE 
            dist = [float("Inf")] * row

            #Parent array to store shortest path tree
            parent = [-1] * row

            # Distance of source vertex from itself is always 0
            dist[src] = 0

            # Add all vertices in queue
            queue = []
            for i in range(row):
                queue.append(i)
            #print(dist)  
            #Find shortest path for all vertices
            while queue:

                # Pick the minimum dist vertex from the set of vertices
                # still in queue
                u = self.minDistance(dist,queue)    
                #print(u+1)
                # remove min element     
                queue.remove(u)


                # Update dist value and parent index of the adjacent vertices of
                # the picked vertex. Consider only those vertices which are still in
                # queue
                for i in range(col):
                    '''Update dist[i] only if it is in queue, there is
                    an edge from u to i, and total weight of path from
                    src to i through u is smaller than current value of
                    dist[i]'''
                    if graph[u][i] and i in queue:
                        if dist[u] + graph[u][i] < dist[i]:
                            dist[i] = dist[u] + graph[u][i]
                            parent[i] = u
                if(u==dest):
                    break
            #parent[src]=-1
            # print the constructed distance array
            self.printSolution(dist,parent,dest)

    # In[72]:


    #This function should be invoked when the vechicle of vechile number 'veh_no' arrived at the destinaion
    def vechiclestop(veh_no):
        if veh_no==1:
            for i in range(1,len(v1path[0])):
                graph[v1path[0][i]][v1path[0][i-1]]=stored_graph[v1path[0][i]][v1path[0][i-1]]
                graph[v1path[0][i-1]][v1path[0][i]]=stored_graph[v1path[0][i-1]][v1path[0][i]]
            v1path.clear()
        if veh_no==2:
            for i in range(1,len(v2path[0])):
                graph[v2path[0][i]][v2path[0][i-1]]=stored_graph[v2path[0][i]][v2path[0][i-1]]
                graph[v2path[0][i-1]][v2path[0][i]]=stored_graph[v2path[0][i-1]][v2path[0][i]]
            v2path.clear()
        if veh_no==3:
            for i in range(1,len(v3path[0])):
                graph[v3path[0][i]][v3path[0][i-1]]=stored_graph[v3path[0][i]][v3path[0][i-1]]
                graph[v3path[0][i-1]][v3path[0][i]]=stored_graph[v3path[0][i-1]][v3path[0][i]]
            v3path.clear()

    g= Graph()

    graph = [[0,3,0,3,1,0,0,0],
            [3,0,3,0,0,1,0,0],
            [0,3,0,3,0,0,1,0],
            [3,0,3,0,0,0,0,1],
            [1,0,0,0,0,1,0,1],
            [0,1,0,0,1,0,1,0],
            [0,0,1,0,0,1,0,1],
            [0,0,0,1,1,0,1,0],]


    kk=1
    vehi=[]
    for i in range(3):
        vehi.append(0)
    import copy
    stored_graph=copy.deepcopy(graph)
    v1path=[]
    v2path=[]
    v3path=[]
    query=0
    v1path_history = []


    t_src=-1
    t_dest=-1
    t_vtype=-1
    while(query<1):
        query=query+1
#        print("Enter the query")
        # calling the image processing code
        botnodes = imageprocessing()
#        print(botnodes,botnodes.shape)

        if vehicle_no == 1:
            source = int(botnodes[[0]])
        elif vehicle_no == 2:
            source = int(botnodes[[1]])
        elif vehicle_no == 3:
            source = int(botnodes[[2]])

        src= source   #put the src and dest in the integer format
        dest= destination  
        vtype= vehicle_no  #Put the vechicle type in this variable in one of {0,1,2}
      
#        print(source)
 #       print(graph)
        graph[previous-1][source-1]=0
        graph[source-1][previous-1]=0
    
        if t_vtype==vtype and t_src==dest and t_dest==src:
            for i in range(1,len(rr)):
                graph[rr[i]][rr[i-1]]=0
                graph[rr[i-1]][rr[i]]=0
        t_src=src
        t_dest=dest
        t_vtype=vtype
        rr=[]
        g.dijkstra(graph,src-1,dest-1)   # The actual shortest path is stored in the array rr. This array can be sent to Central server
        #global vpath
        
        if vtype==1:
            v1path.append(rr)

        if vtype==2:
            v2path.append(rr)
        if vtype==3:
            v3path.append(rr)
        vehi[vtype-1]=1
 #       for i in rr:
 #           print(i+1)
        #print(len(rr))
        for i in range(1,len(rr)):
            graph[rr[i]][rr[i-1]]=0
            graph[rr[i-1]][rr[i]]=0
        #print(graph)
        #print(stored_graph)
        if(vehi[0]==vehi[1] and vehi[0]==vehi[2]):
            graph=copy.deepcopy(stored_graph)
            vehi[0]=0
            vehi[1]=0
            vehi[2]=0
        if query==3:
            print(graph)
            vechiclestop(2)
        #print(graph)

        n0 = (0,-5)
        n1 = (-5,0)
        n2 = (0,5)
        n3 = (5,0)
        n4 = (0,-1)
        n5 = (-1,0)
        n6 = (0,1)
        n7 = (1,0)

        co_ordinates = [n0, n1, n2, n3, n4, n5, n6, n7]
        path_array = []
        for i in rr:
            path_array.append(co_ordinates[i])

        length = len(rr)
        path_array.insert(0,co_ordinates[previous-1])
#        print(path_array)
        previous = rr[len(rr)-1]
        a = final_answer(path_array)
        

        return a


# the image processing function
#code to generate the centroid of nodes marked by aruco markers
def imageprocessing():
    #Obtaining video feed from camera 
    cap = cv2.VideoCapture(0)

    #creating array of node centroids
    node_centroid_array = np.zeros((8,2))
    bot_centroid_array = np.zeros((3,2))
    bot_node_array = np.zeros((3))
    m = 0
    for m in range(0,5):
        init = 0 
        # Capture frame-by-frame
        ret, frame = cap.read()
        #print(frame.shape) #480x640
        # Our operations on the frame come here
        if ret is True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        else:
            continue
        aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
        parameters =  aruco.DetectorParameters_create()
    

        '''    detectMarkers(...)
            detectMarkers(image, dictionary[, corners[, ids[, parameters[, rejectedI
            mgPoints]]]]) -> corners, ids, rejectedImgPoints
        '''
            
        #lists of ids and the corners beloning to each id
        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
        
        # converting to numpy array 
        arr_full = np.array(corners)
        
        # resizing the array to required dimensions
        corners_array = np.resize(arr_full,(len(corners),4,2))

        # initializing node array to zero to store corner values
        node_array = np.zeros((8,4,2))
        bot_array = np.zeros((3,4,2))

#         #creating an array of which stores values of corners corresponding to certain ids
#         #The corner value remains zero if the corner is not detected
        if len(corners)> 0 :
            for i in range(0,len(corners)):
                if ids[i] == 13 :
                    bot_array[0] = corners_array[i]
                elif ids[i] == 14 :
                    bot_array[1] = corners_array[i]
                elif ids[i] == 15 :
                    bot_array[2] = corners_array[i]

        # Caliberated node centroid values. Needs to be caliberated whenever the posistion of camera is drastically altered
	node_centroid_array = np.load('centroids.npy')
        for i in range(0,3):
            
            x_sum = 0
            y_sum = 0
                
            for j in range(0,4):
                x_sum = x_sum + bot_array[i][j][0]
                y_sum = y_sum + bot_array[i][j][1]
                j = j+1

            #To store previous centroid values if node is not detected 
            if x_sum != 0 and y_sum != 0:
                bot_centroid_array[i][0] = x_sum/4
                bot_centroid_array[i][1] = y_sum/4
                

        for i in range(0,3):

            xb = bot_centroid_array[i][0]
            yb = bot_centroid_array[i][1]
                
            for j in range(0,8):
                xn = node_centroid_array[j][0]
                yn = node_centroid_array[j][1]
                r = np.sqrt((xn-xb)**2 + (yn-yb)**2)
                if r < 50:
                    bot_node_array[i] = j+1

#         print(corners_array)
#         print('---------------------------------------')
#         print(ids)
#         print('----------------------------------------')
#         print(node_array)
#         print('-----------------------------------------')
        #print(bot_centroid_array)
        #print('-----------------------------------------')
        print(bot_node_array)
        print('-_-_-_-_-_-_-_','\n\n\n')
        
        #Printing distance between 5 and 6 
        gray = aruco.drawDetectedMarkers(gray, corners,ids)

        #To end camera feed 
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return(bot_node_array)

#b = path_planning(8,8,3)
#print (b)
