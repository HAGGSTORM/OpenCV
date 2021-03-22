import cv2 as cv
import numpy as np


def measure(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("binary",binary)
    contours, hireachy = cv.findContours(binary,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    print(contours)
    for i,contour in enumerate(contours):
        area = cv.contourArea(contour)
        x,y,w,h = cv.boundingRect(contour)
        mm = cv.moments(contour)
        cx = mm['m10']/(mm['m00']+1)
        cy = mm['m01']/(mm['m00']+1)
        cv.circle(img,(np.int(cx),np.int(cy)),3,(0,255,255),-1)
        cv.rectangle(img,(x,y),(x+w,y+h),5)
        print("area %s"%area)
    cv.imshow("measure",img)

src = cv.imread("digit.jpeg")
measure(src)
cv.waitKey(0)
cv.destroyAllWindows()