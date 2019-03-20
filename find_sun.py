import cv2
import matplotlib
import numpy as np
from utilities import *
import scipy.misc
import matplotlib.pyplot as plt

# Mention your sky/cloud image path here. Please make sure that your input image is inside "image" folder.
image_location = './image/2015-09-04-12-22-01-wahrsis3-med.jpg'


im = cv2.imread(image_location)
threshold_value = 240

# This is the main component that performs the computation for sun position in the image. 
(centroid_x,centroid_y) = where_is_sun(im, threshold_value)


plt.figure(1)
plt.imshow(im[:,:, [2,1,0]])
plt.scatter(x=[centroid_y], y=[centroid_x], c='r', s=40)
plt.show()

print ('Note the reference axis definition')
print ('X value = ', str(centroid_y))
print ('Y value = ', str(centroid_x))