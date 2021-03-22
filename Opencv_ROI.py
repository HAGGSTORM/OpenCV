import cv2 as cv


src = cv.imread("2.jpg")
ROI = src[0:200,100:200]
change_ROI = cv.cvtColor(ROI,cv.COLOR_BGR2HSV)
src[0:200,100:200] = change_ROI
cv.imshow("Change_ROI",src)
cv.waitKey(0)
cv.destroyAllWindows()