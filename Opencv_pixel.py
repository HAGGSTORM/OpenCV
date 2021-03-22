import cv2 as cv

src1 = cv.imread("1.jpg")
src2 = cv.imread("2.jpg")
cv.imshow("src1",src1)
cv.imshow("src2",src2)

cv_add = cv.add(src1,src2)
cv.imshow("cv_add",cv_add)

cv_sub = cv.subtract(src1,src2)
cv.imshow("cv_add",cv_sub)

cv.waitKey(0)
cv.destroyAllWindows()


