import cv2 as cv

def bi_demo(img):
    dst = cv.bilateralFilter(img,0,100,15)
    cv.imshow("bi_demo",dst)
def mean_shift(img):
    dst = cv.pyrMeanShiftFiltering(img,15,50)
    cv.imshow("mean_shif",dst)

src = cv.imread("3.jpeg")
cv.imshow("demo",src)
bi_demo(src)
mean_shift(src)
cv.waitKey(0)
cv.destroyAllWindows()