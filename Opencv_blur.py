import cv2 as cv

src = cv.imread("2.jpg")
dst = cv.blur(src,(5,5))
dst1 =cv.medianBlur(src,ksize=5)
cv.imshow("blur",dst1)
cv.waitKey(0)
cv.destroyAllWindows()