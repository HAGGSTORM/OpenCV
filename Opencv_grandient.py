import cv2 as cv
import  numpy as np


def sobel_cal(img):
    grad_x = cv.Sobel(img, cv.CV_32F, 1, 0)
    grad_y = cv.Sobel(img, cv.CV_32F, 0, 1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    gradxy = cv.addWeighted(gradx,0.5,grady,0.5,0)
    cv.imshow("gradient_x",gradx)
    cv.imshow("gradient_y",grady)
    cv.imshow("gradient_xy",gradxy)


def scharr_cal(img):
    grad_x = cv.Scharr(img, cv.CV_32F, 1, 0)
    grad_y = cv.Scharr(img, cv.CV_32F, 0, 1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    gradxy = cv.addWeighted(gradx,0.5,grady,0.5,0)
    cv.imshow("gradient_x",gradx)
    cv.imshow("gradient_y",grady)
    cv.imshow("gradient_xy",gradxy)


def lpls_cal(img):
    dst = cv.Laplacian(img,cv.CV_32F)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow("lpls_cal",lpls)


src = cv.imread("3-s.jpeg")
lpls_cal(src)
cv.waitKey(0)
cv.destroyAllWindows()