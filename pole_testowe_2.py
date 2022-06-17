import cv2 as cv
import os





# dlugosc = 24
img = cv.imread("proba.jpg")
y, x, _ = img.shape


# wielkosc uzglednianego obszaru - 800x1300
h = 200
w = 200

def empty(a):
    pass

cv.namedWindow("Wspolrzedne")
cv.resizeWindow("Wspolrzedne",640,240)
cv.createTrackbar("X1","Wspolrzedne",0,x-w,empty)
cv.createTrackbar("Y1","Wspolrzedne",0,y-h,empty)



while True:
    x1 = cv.getTrackbarPos("X1","Wspolrzedne")
    y1 = cv.getTrackbarPos("Y1","Wspolrzedne")

    img2= img[y1:(y1+h),x1:(x1+w)]

    print(img[y1,x1])
    cv.imshow("o",img2)
    cv.waitKey(1)
