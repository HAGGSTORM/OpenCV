import cv2 as cv
import numpy as np


def threshold_demo(img):#全局阈值
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,108,255,cv.THRESH_TRUNC)
    print(ret)
    cv.imshow("result",binary)


def local_threshold_demo(img):#局部阈值
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    binary = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,25,10)
    cv.imshow("result",binary)


src = cv.imread("3-s.jpeg")
local_threshold_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()