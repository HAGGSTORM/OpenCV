import cv2 as cv
import numpy as np


def contrast_demo(img1, c, b):  # 亮度就是每个像素所有通道都加上b，调节c就是调节对比度
    rows, cols, chunnel = img1.shape
    blank = np.zeros([rows, cols, chunnel], img1.dtype)  # np.zeros(img1.shape, dtype=uint8)
    dst = cv.addWeighted(img1, c, blank, 1-c, b)
    return dst


src = cv.imread("2.jpg")
dst = contrast_demo(src,1.8,10)#c调节对比度，b调节亮度
cv.imshow("src",src)
cv.imshow("brightness",dst)
cv.waitKey(0)
cv.destroyAllWindows()