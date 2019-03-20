import numpy as np 
import cv2
from scipy import ndimage

def where_is_sun(im, threshold_value):


			
			
	# Rotate to correct positions if required
	lx, ly, _ = im.shape
	if lx>ly:
		print ('Rotating')
		im = ndimage.rotate(im, -90)

	# Finding the centroid of sun position polygon
	red = im[:,:,2]
	green = im[:,:,1]
	blue = im[:,:,0]
	all_coord = np.where( red > threshold_value )
	all_coord = np.asarray(all_coord)
	length = np.shape(all_coord)[1]
	sum_x = np.sum(all_coord[0,:])
	sum_y = np.sum(all_coord[1,:])
			
	if (sum_x == 0 or sum_y == 0):
		centroid_x = np.nan
		centroid_y = np.nan
		print ('Sun is not visible in this image')
	else:
		centroid_x = int(sum_x/length)
		centroid_y = int(sum_y/length)
		print ('Sun\'s location in the image is [', str(centroid_x), ',', str(centroid_y), ']')


	return (centroid_x, centroid_y)