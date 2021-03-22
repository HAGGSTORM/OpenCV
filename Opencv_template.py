import cv2 as cv
import numpy as np

def template(temp,src):
    methods = [cv.TM_CCOEFF_NORMED,cv.TM_CCORR_NORMED,cv.TM_SQDIFF_NORMED]
    width,height = temp.shape[:2]
    for md in methods:
        results = cv.matchTemplate(src,temp,md)
        min_val,max_val,min_loc,max_loc = cv.minMaxLoc(results)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0]+width,tl[1]+height)
        cv.rectangle(src,tl,br,(0,0,255),2)
        cv.imshow("template",temp)
        cv.imshow("watch-"+np.str(md),src)

src1 = cv.imread("3.jpg")
src2 = cv.imread("4.jpg")
template(src2,src1)
cv.waitKey(0)
cv.destroyAllWindows()

