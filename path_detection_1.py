#EDGE ID DETECTION
# the image processing function
#code to generate the centroid of nodes marked by aruco markers
import cv2
import numpy as np
import cv2.aruco as aruco
def imageprocessing():
    #Obtaining video feed from camera 
    cap = cv2.VideoCapture(0)

    #creating array of node centroids
    bot_centroid_array = np.zeros((3,2))
    bot_edge_array = np.zeros((3))
    for m in range(0,10):
         
        # Capture frame-by-frame
        ret, frame = cap.read()
        #print(frame.shape) #480x640
        # Our operations on the frame come her
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

        # initializing an array to zero to store corner values
#        edge_array = np.zeros((8,4,2))
	
	# path_list is the number for each path
        path_list = [(1,2),(2,3),(3,4),(1,4),(1,5),(2,6),(3,7),(4,8),(5,6),(6,7),(7,8),(1,8)]
        
	# path_bot indicates which edge, the bot is on
	path_bot = [(0,0),(0,0),(0,0)]              
        
	# Caliberated node centroid values. Needs to be caliberated whenever the posistion of camera is drastically altered
        edge_centroid_array = np.load('calibrate.npy')
        bot_array = np.zeros((3,4,2))
        if len(corners_array)>0:
            for i in range(0,len(corners_array)):   #a loop to iterate over for three bots
                    if ids[i] == 13 : #aruco marker id numberfor bot1
                        bot_array[0] = corners_array[i]
                    elif ids[i] == 14 : #aruco marker id number for bot2
                        bot_array[1] = corners_array[i]
                    elif ids[i] == 15 : #aruco marker id number for bot3
                        bot_array[2] = corners_array[i]
                
	#To obtain the center of the bots
        for i in range(0,3):
            
            x_sum = 0
            y_sum = 0
                
            for j in range(0,4):
                x_sum = x_sum + bot_array[i][j][0] # sum of all x and y coordinates of all the four corners of the square of each aruco marker
                y_sum = y_sum + bot_array[i][j][1]
                j = j+1

            #To store previous centroid values if node is not detected 
            if x_sum != 0 and y_sum != 0:
                bot_centroid_array[i][0] = x_sum/4 # calcu;ation of the centroid values
                bot_centroid_array[i][1] = y_sum/4
                
        # Code snippet to check whether the bot lies on a particular edge or not        
        for i in range(0,3):

            xb = bot_centroid_array[i][0] 
            yb = bot_centroid_array[i][1]
                
            for j in range(0,8):
                xn = edge_centroid_array[j][0]
                yn = edge_centroid_array[j][1]
                r = np.sqrt((xn-xb)**2 + (yn-yb)**2)
                if j == 0 or 1 or 2 or 3:
                    if r < 50:
                        bot_edge_array[i] = j+1
                        path_bot[i] = path_list[j]
                elif j == 4 or 5 or 6 or 7:
                    if r < 30:
                        bot_edge_array[i] = j+1
                        path_bot[i] = path_list[j]
                elif j == 8 or 9 or 10 or 11:
                    if r < 20:
                        bot_edge_array[i] = j+1
                        path_bot[i] = path_list[j]
        
        print(bot_centroid_array)
        print('-----------------------------------------')
        print(bot_edge_array)
        print('-----------------------------------------')
        print(path_bot)
        print('-----------------------------------------')
        
        #Printing distance between 5 and 6 
        gray = aruco.drawDetectedMarkers(gray, corners,ids)

        #To end camera feed 
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return(path_bot)
