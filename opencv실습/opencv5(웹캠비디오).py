import cv2 as cv
import sys

# 웹 캠에서 비디오 읽기
cap = cv.VideoCapture(0)

if not cap.isOpened():
    sys.exit("카메라 연결 실패")

while True:
    ret, frame = cap.read()

    if not ret:
        print("프레임 획득에 실패하여 루프를 나감")
        break

    cv.imshow("video display", frame)

    key = cv.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
