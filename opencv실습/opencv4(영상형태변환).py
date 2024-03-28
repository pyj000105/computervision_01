import cv2 as cv
import sys


# 영상 형태 변환하고 크기 축소하기
img = cv.imread("soccer.jpg")

if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_small = cv.resize(gray, dsize=(0,0), fx= 0.5, fy=0.5)

cv.imwrite("soccer_gray.jpg", gray)
cv.imwrite("soccer_gray_small.jpg", gray_small)

cv.imshow("color image", img)
cv.imshow("gray image", gray)
cv.imshow("gray image small", gray_small)

cv.waitKey()
cv.destroyAllWindows()