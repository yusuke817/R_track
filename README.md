# Flowchart
[![Flowchart](https://i.gyazo.com/23ec5ad130141480e6bdb4d353887a55.jpg)](https://gyazo.com/23ec5ad130141480e6bdb4d353887a55)

# Code
'''
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
'''

# Result on YouTube
[![](https://img.youtube.com/vi/7eQLzrq4qyo/0.jpg)](https://www.youtube.com/watch?v=7eQLzrq4qyo)

# Result on YouTube_3x (Three times faster than the real one)
[![](https://img.youtube.com/vi/atDz4uObtVs/0.jpg)](https://www.youtube.com/watch?v=atDz4uObtVs)
