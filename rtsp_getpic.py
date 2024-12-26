import cv2,time

cap4 = cv2.VideoCapture('')

#cv2.resizeWindow('test4',640,640)
frame_ = 0
print(cap4.isOpened())
while cap4.isOpened():
    time_ = int(time.time())
    ret4, frame4 = cap4.read()
    frame_ += 1
    if frame_ % 3 == 0 :
        cv2.imwrite(rf'./img_save/{time_}.png',frame4)
    frame4 = cv2.resize(frame4,(1080,920))
    cv2.imshow('test4', frame4)

    if cv2.waitKey(1) == ord('q'):
        break
cap4.release()
cv2.destroyAllWindows()
