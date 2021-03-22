import cv2 as cv
import numpy as np


def Gussain_pyramid(img):
    level = 3
    img_pyramid = [img]
    temp = img.copy()
    for i in range(level):
        dst = cv.pyrDown(temp)
        img_pyramid.append(dst)
        #cv.imshow("Gussain_pyramid_level_"+str(i),dst)
        temp = dst.copy()
    return img_pyramid

def lpls_pyramid(imgs):
    level = len(imgs)
    for i in range(level-1):
        print(i)
        dst = cv.pyrUp(imgs[level-1-i])
        print(dst.shape)
        print(imgs[len(imgs)-2-i].shape)
        result = cv.subtract(imgs[len(imgs)-2-i],dst)
        cv.imshow("lpls_pyramid_level"+str(i),result)



src = cv.imread("3.png")
imgs = Gussain_pyramid(src)
for i in range(len(imgs)):
    cv.imshow("Gussain_level_"+str(i),imgs[i])
lpls_pyramid(imgs)
cv.waitKey(0)
cv.destroyAllWindows()