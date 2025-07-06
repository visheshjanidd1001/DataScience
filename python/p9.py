import cv2
cap = cv2.VideoCapture(0)
status , photo = cap.read()
cv2.imshow("vishesh photo" , photo)
cv2.waitkey(5000)
cv2.destroyAllWindows()
