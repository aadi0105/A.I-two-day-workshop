import cv2
cap=cv2.VideoCapture(0)
while True:
    status, photo=cap.read()
    #for giving cropped video of ypur face uncomment below line 
    #newphoto = photo[120:680, 135:500]
    cv2.imshow('hii',newphoto)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
cap.release()