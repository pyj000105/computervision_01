import cv2 as cv
import sys
import numpy as np



# 페인팅 기능 만들기 9번
BrushSize = 5
LColor, RColor = (255, 0, 0), (0, 0, 255)

def paintitng(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x,y), BrushSize, LColor, -1)
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x,y), BrushSize, RColor, -1)
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        cv.circle(img, (x,y), BrushSize, LColor, -1)        
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_RBUTTON:
        cv.circle(img, (x,y), BrushSize, RColor, -1)

    cv.imshow('Painting', img)

img = cv.imread("soccer.jpg")

if img is None:
     sys.exit("파일을 찾을 수 없습니다.")

cv.namedWindow('Painting')
cv.imshow('Painting', img)
cv.setMouseCallback('Painting',paintitng)

while(True):
    if cv.waitKey(1)== ord('q'):
        cv.destroyAllWindows()
        break