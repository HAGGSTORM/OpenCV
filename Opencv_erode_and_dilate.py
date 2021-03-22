import cv2 as cv
import numpy as np


def cv_erode(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("erode_binary",binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    dst = cv.erode(binary,kernel=kernel)
    cv.imshow("erode",dst)


def cv_dilate(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("dilate_binary",binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    dst = cv.dilate(binary,kernel=kernel)
    cv.imshow("dilate",dst)


src = cv.imread("digit.jpeg")
cv_erode(src)
cv_dilate(src)
cv.waitKey(0)
cv.destroyAllWindows()