import cv2
cap=cv2.VideoCapture(0)
status,photo1=cap.read()
cv2.imwrite('second.png',photo1)
cap.release()
cv2.imshow('image-1',photo1)
cv2.waitKey()
cv2.destroyAllWindows()
cap=cv2.VideoCapture(0)
status,photo2=cap.read()
cv2.imwrite('third.png',photo2)
cap.release()
cv2.imshow('image-2',photo2)
cv2.waitKey()
cv2.destroyAllWindows()
croppedphoto1 = photo1[120:680, 135:500]
cv2.imshow('cropped-image-1',croppedphoto1)
cv2.waitKey()
cv2.destroyAllWindows()
croppedphoto2 = photo2[120:680, 135:500]
cv2.imshow('cropped-image-2',croppedphoto2)
cv2.waitKey()
cv2.destroyAllWindows()
temp = croppedphoto2 + croppedphoto1
photo1[120:680, 135:500] = croppedphoto2
cv2.imshow('swapped-image-1',photo1)
cv2.waitKey()
cv2.destroyAllWindows()
photo2[120:680, 135:500] = temp-croppedphoto2
cv2.imshow('swapped-image-2',photo2)
cv2.waitKey()
cv2.destroyAllWindows()