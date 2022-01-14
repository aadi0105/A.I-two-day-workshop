import cv2
cap=cv2.VideoCapture(0)
status, photo1=cap.read()
cv2.imwrite('one.png',photo1)
cap.release()
cv2.imshow('myimage',photo1)
cv2.waitKey()
cv2.destroyAllWindows()
newphoto1 = photo1[100:300 , 200:400]
cv2.imshow('image',newphoto1)
cv2.waitKey()
cv2.destroyAllWindows()