import math
import copy
u = 0
	
v1path = []
v2path = []
v3path = []
stored_graph= [[0,3,0,3,1,0,0,0],
            [3,0,3,0,0,1,0,0],
            [0,3,0,3,0,0,1,0],
            [3,0,3,0,0,0,0,1],
            [1,0,0,0,0,1,0,1],
            [0,1,0,0,1,0,1,0],
            [0,0,1,0,0,1,0,1],
            [0,0,0,1,1,0,1,0],]

    
def clear_path(vehicle_no, gph):
    global graph, stored_graph, v1path, v2path, v3path, u
    
    graph = gph
    
    if vehicle_no == 1:
	for i in range(1,len(v1path)):
	        graph[v1path[i]-1][v1path[i-1]-1]=stored_graph[v1path[i]-1][v1path[i-1]-1]
	        graph[v1path[i-1]-1][v1path[i]-1]=stored_graph[v1path[i-1]-1][v1path[i]-1]

    if vehicle_no == 2:
	for i in range(1,len(v2path)):
	        graph[v2path[i]-1][v2path[i-1]-1]=stored_graph[v2path[i]-1][v2path[i-1]-1]
	        graph[v2path[i-1]-1][v2path[i]-1]=stored_graph[v2path[i-1]-1][v2path[i]-1]
 
    if vehicle_no == 3:
	for i in range(1,len(v3path)):
	        graph[v3path[i]-1][v3path[i-1]-1]=stored_graph[v3path[i]-1][v3path[i-1]-1]
	        graph[v3path[i-1]-1][v3path[i]-1]=stored_graph[v3path[i-1]-1][v3path[i]-1]

    return graph

def path_planning(edge_no, vehicle_no, source, prev, gph):
    global graph, stored_graph, v1path, v2path, v3path, previous_1, previous_2, previous_3, source_1, source_2, source_3, u
    graph = gph
  
    n0 = (0,-5)
    n1 = (-5,0)
    n2 = (0,5)
    n3 = (5,0)
    n4 = (0,-1)
    n5 = (-1,0)
    n6 = (0,1)
    n7 = (1,0)
    co_ordinates = [n0, n1, n2, n3, n4, n5, n6, n7]

    def get_instruction(rr, previous, co_ordinates):
	    
	    path_array = []
	    for i in rr:
	    	path_array.append(co_ordinates[i]) 
	    path_array.insert(0,co_ordinates[previous-1])
	    return path_array


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
	                if angle<=90:
	                        turn = turn_complement(turn)
	            array.append(turn)
	 	    array.append('F')   
	    if not any(array):	
	    	message = ''
	    else:
	    	message = ''.join(array)                
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
+	representation'''
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
		#print u
		if u>=0:    
	        	queue.remove(u)
		else:
			break

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
	    #print "x"
	    #parent[src]=-1
	    # print the constructed distance array
	    if u>=0:
	    	self.printSolution(dist,parent,dest)
   
    if vehicle_no == 1:
	    v1path = []
	    g= Graph()
	    source_1 = source
	    previous_1 = prev
	    #graph1 = graph
	    src= source_1   #put the src and dest in the integer format
	    dest= edge_no[0]  
	    vtype= vehicle_no

	    #t_src=-1
	    #t_dest=-1
	    #t_vtype=-1

	    m = edge_no[0]
	    n = edge_no[1]
	    graph[m-1][n-1]=0
	    graph[n-1][m-1]=0
	    graph[previous_1-1][src-1]=0
	    graph[src-1][previous_1-1]=0

	    #if t_vtype==vtype and t_src==dest and t_dest==src:
	    #	    for i in range(1,len(rr)):
	    #		graph[rr[i]][rr[i-1]]=0
	    #		graph[rr[i-1]][rr[i]]=0
	    #t_src=src
	    #t_dest=dest
	    #t_vtype=vtype
	    
	    rr=[]
	    g.dijkstra(graph,src-1,dest-1)   # The actual shortest path is stored in the array rr. This array can be sent to Central server
		#global vpath
	    rr1 = rr
	    #print rr1
	    if rr:
		    for i in rr1:
		    	v1path.append(i+1)
		    path_array = get_instruction(rr1, previous_1, co_ordinates)
		    #print rr1
		    #print path_array
		    str1 = final_answer(path_array)
		    
		    #first as soon as the path is alloted free the path of current-previous node
		    graph[previous_1-1][src-1]=stored_graph[previous_1-1][src-1]
		    graph[src-1][previous_1-1]=stored_graph[src-1][previous_1-1]

		    #update the graph to block paths based on the path obtained for first half
		    for i in range(1,len(rr1)):
			graph[rr[i]][rr[i-1]]=0
			graph[rr1[i-1]][rr[i]]=0
		    
		    previous_1 = rr[len(rr)-2] + 1

		    #get path from djikstra for the edge co-ordinates
		    rr = []
		    graph[m-1][n-1] = stored_graph[m-1][n-1]
		    graph[n-1][m-1] = stored_graph[n-1][m-1]
		    g.dijkstra(graph,m-1,n-1)
		    rr2 = rr
		    path_array = get_instruction(rr2, previous_1, co_ordinates)
		    #print rr2
		    #print path_array
		    str2 = final_answer(path_array)

		    #to update graph to block paths based on path obtained for second half
		    for i in range(1,len(rr2)):
			graph[rr[i]][rr[i-1]]=0
			graph[rr[i-1]][rr[i]]=0

		    #update the previous node value for next iteration
		    previous_1 = rr2[len(rr2)-2] + 1
		    
		    #print graph
		    rr3 = rr1+rr2
		    #print rr3
		    source_1 = rr2[1]+1
		    #print v1path
		    ans = str1+str2
		    ans = ans[:-1]
		    return (ans+'S', source_1, previous_1, graph)
	    else:
		    graph[m-1][n-1]=stored_graph[m-1][n-1]
	            graph[n-1][m-1]=stored_graph[n-1][m-1]
		    return ("no path", source_1, previous_1, graph)

    if vehicle_no == 2:
	    v2path = []
	    g= Graph()
	    source_2 = source
	    previous_2 = prev
	    #graph1 = graph
	    src= source_2   #put the src and dest in the integer format
	    dest= edge_no[0]  
	    vtype= vehicle_no

	    #t_src=-1
	    #t_dest=-1
	    #t_vtype=-1

	    m = edge_no[0]
	    n = edge_no[1]
	    graph[m-1][n-1]=0
	    graph[n-1][m-1]=0
	    graph[previous_2-1][src-1]=0
	    graph[src-1][previous_2-1]=0

	    #if t_vtype==vtype and t_src==dest and t_dest==src:
	    #	    for i in range(1,len(rr)):
	    #		graph[rr[i]][rr[i-1]]=0
	    #		graph[rr[i-1]][rr[i]]=0
	    #t_src=src
	    #t_dest=dest
	    #t_vtype=vtype
	    
	    rr=[]
	    g.dijkstra(graph,src-1,dest-1)   # The actual shortest path is stored in the array rr. This array can be sent to Central server
		#global vpath
	    rr1 = rr
	    #print rr1
	    if rr:
		    for i in rr1:
		    	v2path.append(i+1)
		    path_array = get_instruction(rr1, previous_2, co_ordinates)
		    #print rr1
		    #print path_array
		    str1 = final_answer(path_array)
		    
		    #first as soon as the path is alloted free the path of current-previous node
		    graph[previous_2-1][src-1]=stored_graph[previous_2-1][src-1]
		    graph[src-1][previous_2-1]=stored_graph[src-1][previous_2-1]

		    #update the graph to block paths based on the path obtained for first half
		    for i in range(1,len(rr1)):
			graph[rr[i]][rr[i-1]]=0
			graph[rr1[i-1]][rr[i]]=0
		    
		    previous_2 = rr[len(rr)-2] + 1

		    #get path from djikstra for the edge co-ordinates
		    rr = []
		    graph[m-1][n-1] = stored_graph[m-1][n-1]
		    graph[n-1][m-1] = stored_graph[n-1][m-1]
		    g.dijkstra(graph,m-1,n-1)
		    rr2 = rr
		    path_array = get_instruction(rr2, previous_2, co_ordinates)
		    #print rr2
		    #print path_array
		    str2 = final_answer(path_array)

		    #to update graph to block paths based on path obtained for second half
		    for i in range(1,len(rr2)):
			graph[rr[i]][rr[i-1]]=0
			graph[rr[i-1]][rr[i]]=0

		    #update the previous node value for next iteration
		    previous_2 = rr2[len(rr2)-2] + 1
		    
		    #print graph
		    rr3 = rr1+rr2
		    #print rr3
		    source_2 = rr2[1]+1
		    #print v2path
		    ans = str1+str2
                    ans = ans[:-1]
		    return ans+'S', source_2, previous_2, graph
	    else:
		    graph[m-1][n-1]=stored_graph[m-1][n-1]
	            graph[n-1][m-1]=stored_graph[n-1][m-1]
		    return ("no path", source_2, previous_2, graph)

    if vehicle_no == 3:
	    v3path = []
	    g= Graph()
	    source_3 = source
	    previous_3 = prev
	    #graph1 = graph
	    src= source_3   #put the src and dest in the integer format
	    dest= edge_no[0]  
	    vtype= vehicle_no

	    #t_src=-1
	    #t_dest=-1
	    #t_vtype=-1

	    m = edge_no[0]
	    n = edge_no[1]
	    graph[m-1][n-1]=0
	    graph[n-1][m-1]=0
	    graph[previous_3-1][src-1]=0
	    graph[src-1][previous_3-1]=0

	    #if t_vtype==vtype and t_src==dest and t_dest==src:
	    #	    for i in range(1,len(rr)):
	    #		graph[rr[i]][rr[i-1]]=0
	    #		graph[rr[i-1]][rr[i]]=0
	    #t_src=src
	    #t_dest=dest
	    #t_vtype=vtype
	    
	    rr=[]
	    g.dijkstra(graph,src-1,dest-1)   # The actual shortest path is stored in the array rr. This array can be sent to Central server
		#global vpath
	    rr1 = rr
	    #print rr1
	    if rr:
		    for i in rr1:
		    	v3path.append(i+1)
		    path_array = get_instruction(rr1, previous_3, co_ordinates)
		    #print rr1
		    #print path_array
		    str1 = final_answer(path_array)
		    
		    #first as soon as the path is alloted free the path of current-previous node
		    graph[previous_3-1][src-1]=stored_graph[previous_3-1][src-1]
		    graph[src-1][previous_3-1]=stored_graph[src-1][previous_3-1]

		    #update the graph to block paths based on the path obtained for first half
		    for i in range(1,len(rr1)):
			graph[rr[i]][rr[i-1]]=0
			graph[rr1[i-1]][rr[i]]=0
		    
		    previous_3 = rr[len(rr)-2] + 1

		    #get path from djikstra for the edge co-ordinates
		    rr = []
		    graph[m-1][n-1] = stored_graph[m-1][n-1]
		    graph[n-1][m-1] = stored_graph[n-1][m-1]
		    g.dijkstra(graph,m-1,n-1)
		    rr2 = rr
		    path_array = get_instruction(rr2, previous_3, co_ordinates)
		    #print rr2
		    #print path_array
		    str2 = final_answer(path_array)

		    #to update graph to block paths based on path obtained for second half
		    for i in range(1,len(rr2)):
			graph[rr[i]][rr[i-1]]=0
			graph[rr[i-1]][rr[i]]=0

		    #update the previous node value for next iteration
		    previous_3 = rr2[len(rr2)-2] + 1
		    
		    #print graph
		    rr3 = rr1+rr2
		    #print rr3
		    source_3 = rr2[1]+1
		    #print v3path
		    ans = str1+str2
                    ans = ans[:-1]
		    return ans+'S', source_3, previous_3, graph
	    else:
		    graph[m-1][n-1]=stored_graph[m-1][n-1]
	            graph[n-1][m-1]=stored_graph[n-1][m-1]
		    return ("no path", source_3, previous_3, graph)
'''	    
graph = [[0,3,0,3,1,0,0,0],
            [3,0,3,0,0,1,0,0],
            [0,3,0,3,0,0,1,0],
            [3,0,3,0,0,0,0,1],
            [1,0,0,0,0,1,0,1],
            [0,1,0,0,1,0,1,0],
            [0,0,1,0,0,1,0,1],
            [0,0,0,1,1,0,1,0],]
stored_graph= [[0,3,0,3,1,0,0,0],
            [3,0,3,0,0,1,0,0],
            [0,3,0,3,0,0,1,0],
            [3,0,3,0,0,0,0,1],
            [1,0,0,0,0,1,0,1],
            [0,1,0,0,1,0,1,0],
            [0,0,1,0,0,1,0,1],
            [0,0,0,1,1,0,1,0],]
previous_1 = 2
previous_2 = 3
previous_3 = 1

source_1 = 1
source_2 = 2
source_3 = 2  

for i in range(0,3):
	if i == 0:	
		
		edge_no = [2,1]
		vehicle_no = 1

		b = path_planning(edge_no,vehicle_no)
		print b
		if vehicle_no == 1:
			print v1path
		elif vehicle_no == 2:
			print v2path
		elif vehicle_no == 3:
			print v3path
		#clear_path(1)
		
	if i == 1:
		
		edge_no = [3,7]
		vehicle_no = 2
		
		b = path_planning(edge_no,vehicle_no)
		print b
		if vehicle_no == 1:
			print v1path
		elif vehicle_no == 2:
			print v2path
		elif vehicle_no == 3:
			print v3path
		print v1path
		clear_path(1)
	
	if i == 2:
		
		edge_no = [8,5]
		vehicle_no = 3
			
		b = path_planning(edge_no, vehicle_no)
		print b
		if vehicle_no == 1:
			print v1path
		elif vehicle_no == 2:
			print v2path
		elif vehicle_no == 3:
			print v3path
		clear_path(2)

'''
