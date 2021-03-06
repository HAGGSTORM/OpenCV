import cv2 as cv
import numpy as np

src = cv.imread("6.jpg")
cv.imshow("input", src)
gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
ret, binary = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV|cv.THRESH_OTSU)
cv.imshow("binary", binary)

# 形态学操作
se = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
open_img = cv.morphologyEx(binary, cv.MORPH_OPEN, se, iterations=2)

# sure background area
sure_bg = cv.dilate(open_img,se,iterations=3)
cv.imshow("sure_bg", sure_bg)

# 距离变换
dist_transform = cv.distanceTransform(open_img, cv.DIST_L2, 5)
ret, sure_fg = cv.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
cv.imshow("distance transform", dist_transform/50)
cv.imshow("sure_fg", sure_fg)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv.subtract(sure_bg, sure_fg)

# 连通组件标记 - 发现markers
ret, markers = cv.connectedComponents(sure_fg)
markers = markers+1

# 设定边缘待分割区域
markers[unknown==255] = 0

# 分水岭分割
markers = cv.watershed(src,markers)
src[markers == -1] = [0,0,255]
cv.imshow("result", src)

cv.waitKey(0)
cv.destroyAllWindows()