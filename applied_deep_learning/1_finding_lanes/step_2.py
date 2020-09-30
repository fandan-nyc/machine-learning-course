 # python -m pip install opencv-contrib-python
 # leverage opencv 
 # continue from step 1
import cv2
import numpy as np
import matplotlib.pyplot as plt


# read the image

def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny


def region_of_interest(image):
    height = image.shape[0]
    poligons = np.array([[(200, height),(1100, height), (500, 250)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, poligons, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
    return line_image


def make_coordinates(image, line_param):
    slope, intercept = line_param
    y1 = image.shape[0]
    y2 = int(y1 * 3/5)
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    return np.array([x1, y1, x2, y2])


def average_slop_intercept(image, lines):
    left_fit = []
    right_fit = []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        slope = parameters[0]
        intercept = parameters[1]
        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
    left_fit_avg = np.average(left_fit, axis=0)
    right_fit_avg = np.average(right_fit, axis=0)
    left_line = make_coordinates(image, left_fit_avg)
    right_line = make_coordinates(image, right_fit_avg)
    return np.array([left_line, right_line])


# image = cv2.imread('test_image.jpg')
# read the doc for Probablistic Hough Line Trans 

# to detect the straight line, we need hough transform
# y = mx + b -> hough transform -> coordinates of m and b
# through each dot, there are infinite number of lines going through, so in hough space, it is a straight line
# each dot has a straight line, if 2 dots are in the sdame line, their hough space line should have a cross
# to ensure that multiple dots are in the same line roughly, we have a grid and vote for each small cell
# say, 5 dots, 20 intersections, if they all fall into the same cell, then we know that they are roughly in a straight line

# note that, in cartesian coordinates, we cannot have a vertical line
# but we can leverage the polar coordinates, to identify dots in the same line, we can leverage the grid idea above
def lane_detection(image):
    lane_image = np.copy(image)
    canny_image = canny(lane_image)
    roi = region_of_interest(canny_image)
    lines = cv2.HoughLinesP(roi, 2, np.pi/180, 100, minLineLength=40, maxLineGap=5)
    avg_lines = average_slop_intercept(image, lines)
    line_image = display_lines(lane_image, avg_lines)
    combo_image = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1)
    cv2.imshow("result", combo_image)

cap = cv2.VideoCapture("test_video.mp4")
while cap.isOpened():
    _, frame = cap.read()
    lane_detection(frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    
