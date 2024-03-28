import cv2 as cv
import sys

# 비디오에서 수집한 영상 이어 붙이기
cap = cv.VideoCapture(0)

if not cap.isOpened():
    sys.exit("카메라 연결 실패")

frames = []

while True:
    ret, frame = cap.read()

    if not ret:
        print("프레임 획득에 실패하여 루프를 나감")
        break

    cv.imshow("video display", frame)

    key = cv.waitKey(1)
    if key == ord("c"):
        frames.append(frame)

    elif key == ord("q"):
        break

cap.release()
cv.destroyAllWindows()

if len(frames) > 0:
    imgs = frames[0]
    for i in range(1, min(3, len(frames))):
        img = np.hstack((imgs, frames[i]))
    
    cv.imshow("collected images", imgs)

    cv.waitKey()
    cv.destroyAllWindows()

print(len(frames))
print(frames[0].shape)
print(type(imgs))
print(imgs.shape)

