import cv2 as cv
import numpy as np

src = cv.imread("2.jpg")
h,w = src.shape[:2]
print(src.dtype)
blank = np.zeros([h,w],dtype=np.uint8)
blank[100:400,100:400] = 255
cv.imshow("blank",blank)
cv.waitKey(0)
cv.destroyAllWindows()