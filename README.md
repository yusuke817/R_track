# Flowchart
[![Flowchart](https://i.gyazo.com/23ec5ad130141480e6bdb4d353887a55.jpg)](https://gyazo.com/23ec5ad130141480e6bdb4d353887a55)

# Code (rt_1101)
I made the file called "rt_1101." I added many comments in the code, so I would like you to read. 

<br>
Mainly, I did two things. ①One was to get the information on golden boxes in the function of "find_token." (Line71-92) ②The other was implementation of catching silver boxes and avoiding the wall composed of golden boxes done in main function. (Line95-137)
<br>
①Getting the information on golden boxes

<br>
②Implementation of catching silver boxes and avoiding the wall
'''
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
'''

# Result on YouTube
Result is shown in the video below.
<br>
[![](https://img.youtube.com/vi/7eQLzrq4qyo/0.jpg)](https://www.youtube.com/watch?v=7eQLzrq4qyo)

# Result on YouTube_3x (Three times faster than the real one)
The video above takes much time, so I made the video three times faster.
<br>
[![](https://img.youtube.com/vi/atDz4uObtVs/0.jpg)](https://www.youtube.com/watch?v=atDz4uObtVs)
