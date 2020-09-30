 # python -m pip install opencv-contrib-python
 # leverage opencv 
import cv2
import numpy as np


# read the image
image = cv2.imread('test2.jpg')
#cv2.imshow('result', image)
#cv2.waitKey(0) # wait till we press key 0 to quit


# edge detection
# sharp change in intensity in adjacent pixels
# gradient -> measure of change in brightness over adjacent pixels
# strong gradient -> 0 -> 255, small gradient 0 -> 15
# change the original image => gradient image, find out the edge

# step 1: convert a colorful image to a grayscale image 
#         it is because the original image has 3 channels, red yellow and blue
#         greyscale image has only one channel. so it is easier, faster and less computational intensive.


lane_image = np.copy(image)
gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)

# step 2: reduce noise
# guassian blur, guassian smoothing, reduce noise, reduce details
# kernel convolution: kernel is a small matrix, used for blurring/sharpening the image

blur = cv2.GaussianBlur(gray, (5,5), 0)

# step 3: canny edge detection
# for adjacenct pixels, calculate the gradient (derivative)
# if the gradient > high threshold, edge
# if the gradient < low threshold, not edge
# if the gradient between low and high, consider as edge when it is adjacent to an edge pixel
canny = cv2.Canny(blur, 50, 150)
cv2.imshow("result", canny)
cv2.waitKey(0)
