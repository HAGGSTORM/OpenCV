import cv2 as cv
import numpy as np
src = cv.imread("2.jpg")
src_hsv = cv.cvtColor(src,cv.COLOR_BGR2HSV)
lower = np.array([100,43,46])
upper = np.array([124,255,255])
mask = cv.inRange(src_hsv,lowerb=lower,upperb=upper)
cv.imshow("hsv",src_hsv)
cv.imshow("capture",mask)
cv.waitKey(0)
cv.destroyAllWindows()