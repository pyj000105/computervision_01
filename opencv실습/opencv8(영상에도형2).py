import cv2 as cv
import sys

# 영상에 도형을 그리고 글씨 쓰기 2
img = cv.imread("soccer.jpg")

if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

def draw(event, x ,y, flags, param):
    global ix,iy
 
    if event == cv.EVENT_LBUTTONDOWN:
          ix,iy=x,y

    elif event == cv.EVENT_RBUTTONDOWN:
          cv.rectangle(img, (ix,iy), (x,y), (0,0,255), 2)

    cv.imshow("Drawing", img)

cv.namedWindow("Drawing")
cv.imshow("Drawing", img)

cv.setMouseCallback("Drawing", draw)

while(True):
    if cv.waitKey(1)==ord("q"):
        cv.destroyAllWindows()
        break