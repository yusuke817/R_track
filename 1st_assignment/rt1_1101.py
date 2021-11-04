 from __future__ import print_function

import time
from sr.robot import *

"""
Exercise 3 python script

We start from the solution of the exercise 2
Put the main code after the definition of the functions. The code should make the robot:
	- 1) find and grab the closest silver marker (token)
	- 2) move the marker on the right
	- 3) find and grab the closest golden marker (token)
	- 4) move the marker on the right
	- 5) start again from 1

The method see() of the class Robot returns an object whose attribute info.marker_type may be MARKER_TOKEN_GOLD or MARKER_TOKEN_SILVER,
depending of the type of marker (golden or silver). 
Modify the code of the exercise2 to make the robot:

1- retrieve the distance and the angle of the closest silver marker. If no silver marker is detected, the robot should rotate in order to find a marker.
2- drive the robot towards the marker and grab it
3- move the marker forward and on the right (when done, you can use the method release() of the class Robot in order to release the marker)
4- retrieve the distance and the angle of the closest golden marker. If no golden marker is detected, the robot should rotate in order to find a marker.
5- drive the robot towards the marker and grab it
6- move the marker forward and on the right (when done, you can use the method release() of the class Robot in order to release the marker)
7- start again from 1

	When done, run with:
	$ python run.py exercise3.py

"""


a_th = 10.0 # I did not change the value
""" float: Threshold for the control of the orientation"""

silver_d_th = 0.4   #// threthold for finding the silver box. Of cource, it is better that the value is as big as possible for 
golden_d_th = 0.75  #//  If this value is too small, the risk of the robot crashing against he wall becomes big. If this value is too big, the robot cannot go forward smoothly since the movement for avoiding the wall is too many.  I decided the value experimentally.
""" float: Threshold for the control of the linear distance"""

R = Robot()
""" instance of the class Robot"""

def drive(speed, seconds):
    """
    Function for setting a linear velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed  #power? torque?
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def turn(speed, seconds):
    """
    Function for setting an angular velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def find_token():
    """
    Function to find the closest token

    Returns:
	dist (float): distance of the closest token (-1 if no token is detected)
	rot_y (float): angle between the robot and the token (-1 if no token is detected)
    """
    silver_dist=100
    golden_dist=100
    for token in R.see():  #Not only the information on silver boxes, but also the one on golden boxes are needed to realize the tasks.
        if  (token.dist < silver_dist ) &  (token.info.marker_type==MARKER_TOKEN_SILVER ) & (-120 < token.rot_y < 105):  #  In order for the robot not to  detect the silver box picked up, the angle limitation was implemented
            silver_dist=token.dist
	    silver_rot_y=token.rot_y
	elif (token.dist < golden_dist ) &  (token.info.marker_type==MARKER_TOKEN_GOLD):  #When the robot is close to golden boxes, the information on golden boxes should be sent to main function. Also, angle limitation is not needed for  avoiding the wall composed of the golden boxes.
	    golden_dist=token.dist
	    golden_rot_y=token.rot_y
	    
    if silver_dist==100:
	return -1, -1,-1, -1
    else:
   	return silver_dist, silver_rot_y, golden_dist, golden_rot_y


while 1:
    silver_dist, silver_rot_y, golden_dist, golden_rot_y= find_token()  # we look for markers
    if silver_dist==-1:
        print("I don't see any token!!")
	exit()  # if no markers are detected, the program ends
    elif golden_dist <golden_d_th:  # if the robot is too close to the wall which mean golden boxes, it should go backward and change directions
    	print("Watch out!")
	if golden_rot_y > 0: # if the robot is not well aligned with the token, we move it on the left or on the right. In this case the wall is located on the right side of the robot, so the robot should turn left.
	   print("Left a bit...")
	   #drive(-20,1)
	   drive(-7.5, 1)	   
	   turn(-5, 1.0)
	   drive(10, 2)
	else: #In this case the wall is located on the left side of the robot, so the robot should turn right.
	   print("Right a bit...")
	   #drive(-20,1)
	   drive(-7.5, 1)
	   turn(+5, 1.0)
	   drive(10,1.5)
	continue # going back to -> 96, until the robot becomes far from the wall, the robot should try to change its direction
	 # should not modify from114-121ß
    elif silver_dist <silver_d_th:  #
        print("Found it!")
        R.grab() # if we are close to the token, we grab it.
        print("Gotcha!")
        turn(+15, 4.0)
        R.release()
        turn(+0, 2.0)
        drive(-10, 2.0)
        turn(-15, 4.0)
        drive(15, 2.5)
        #Grabbing the box, turning clockwise direction, leaving the box, going backward , turning counter-clockwise direction,and moving forward
    elif -a_th<= silver_rot_y <= a_th: # if the robot is well aligned with the token, we go forward
        print("Ah, here we are!.")
        drive(20, 0.5)#going straight to the box
    elif silver_rot_y < -a_th: # if the robot is not well aligned with the token, we move it on the left or on the right
        print("Left a bit...")
        turn(-10, 0.1)
        drive(10, 0.4)
    elif silver_rot_y > a_th:
        print("Right a bit...")
        turn(+10, 0.1)
        drive(10, 0.4)



