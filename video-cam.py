import cv2
cap=cv2.VideoCapture(0)
while True:
    status, photo=cap.read()
    cv2.imshow('hii',photo)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
cap.release()