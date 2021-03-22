import cv2 as cv
import numpy as np

def edge(img):
    blur = cv.GaussianBlur(img,(3,3),0)
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    xgrad = cv.Sobel(gray,cv.CV_16SC1,1,0)
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    dst = cv.Canny(xgrad,ygrad,50,150)
    cv.imshow("Canny_edge",dst)


src = cv.imread("3-s.jpeg")
edge(src)
cv.waitKey(0)
cv.destroyAllWindows()